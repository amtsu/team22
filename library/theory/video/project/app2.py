import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = '5973353632:AAFCatfGzjItHliXgPe9ybY3RDmOL-Er0sk'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#from flask import Flask
#from redis import Redis


import torch
import pytorch_lightning as pl
import torchvision

from PIL import Image

import numpy as np

import matplotlib.pyplot as plt

class RetinaRehead(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.model = torchvision.models.detection.retinanet_resnet50_fpn_v2(weights='DEFAULT')
        self.detector = torch.nn.Conv2d(256, 10, kernel_size=3, padding=1)


    def forward(self, input):
        res = self.model.backbone.forward(input)
        res = res['0']
        res = self.detector.forward(res)
        return res
    
    
class PLModel(pl.LightningModule):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def forward(self, input):
        return self.model.forward(input)
    

def decode_result(datum, threshold=1.0, r=8, iou_threshold=0.7):
    bboxes = {'boxes': [], 'scores': [], 'labels': []}
    datum = {0: datum[:5, :, :], 
             1: datum[5:, :, :]}

    for label in [0, 1]:
        mask = (datum[label][0, :, :] >= threshold)

        x_cell = torch.arange(mask.shape[1], device=datum[label].device)
        y_cell = torch.arange(mask.shape[0], device=datum[label].device)

        y_cell, x_cell = torch.meshgrid(y_cell, x_cell)

        x_cell = x_cell[mask]
        y_cell = y_cell[mask]

        x_shift = datum[label][2, :, :][mask]
        y_shift = datum[label][1, :, :][mask]

        x = (x_cell + x_shift) * r
        y = (y_cell + y_shift) * r

        w = datum[label][4, :, :][mask].exp() * r
        h = datum[label][3, :, :][mask].exp() * r

        scores = datum[label][0, :, :][mask]


        for index in range(len(x)):
            bboxes['boxes'].append([x[index] - w[index]/2, 
                         y[index] - h[index]/2, 
                         x[index] + w[index]/2, 
                         y[index] + h[index]/2])
            bboxes['scores'].append(scores[index])
            bboxes['labels'].append(label)

    bboxes['boxes'] = torch.tensor(bboxes['boxes']).reshape([-1, 4])
    bboxes['scores'] = torch.tensor(bboxes['scores'])
    bboxes['labels'] = torch.tensor(bboxes['labels'])

    to_keep = torchvision.ops.nms(bboxes['boxes'], bboxes['scores'], iou_threshold=iou_threshold)

    bboxes['boxes'] = bboxes['boxes'][to_keep]
    bboxes['scores'] = bboxes['scores'][to_keep]
    bboxes['labels'] = bboxes['labels'][to_keep]

    return bboxes


def decode_batch(batch, threshold=0.1, iou_threshold=0.3):
    res = []
    for index in range(batch.shape[0]):
        res.append(decode_result(batch[index], 
                   threshold=threshold, 
                   iou_threshold=iou_threshold))
    return res

def draw_box(coords, label):
    # print(coords)
    # print(label)
    # return None
    x = np.array((coords[0], coords[2]))
    y = np.array((coords[1], coords[3]))
    color = 'g'
    if label == 0:
        color = 'r'

    plt.plot(x.mean(), y.mean(), '*' + color)

    plt.plot([x[0], x[0]], [y[0], y[1]], color)
    plt.plot([x[1], x[1]], [y[0], y[1]], color)
    plt.plot([x[0], x[1]], [y[0], y[0]], color)
    plt.plot([x[0], x[1]], [y[1], y[1]], color)
    # plt.__text(x[0], y[0], label, backgroundcolor='red')


import cv2
    

    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #output3.mp4
    #newFile = update.message.effective_attachment.get_file()
    #newFile.download('data/output11.mp4')

    #file = await context.bot.get_file(update.message.document)
    #await file.download_to_drive('file_name')

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Detector newFile")
    #await context.bot.send_document(chat_id=update.effective_chat.id, document=open('data/output11.mp4', 'rb'))

    #context.bot.get_file(update.message.document).download()

    # writing to a custom file
    with open("data/file.doc", 'wb') as f:
        f.write('222')
    #    context.bot.get_file(update.message.document).download(out=f)


    await context.bot.send_message(chat_id=update.effective_chat.id, text="Detector cars")


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):


    device = 'cpu'
    state = torch.load(
        'data/detector_checkpoint.ckpt',
        map_location='cpu')
    state = state['state_dict']
    model = PLModel(RetinaRehead())
    model.load_state_dict(state)
    model = model.model.to(device).eval()
 
    try:
        try:
            file_id = update.message.photo[-1].file_id
            print(file_id)
            new_file = await context.bot.get_file(file_id)

        except:
            #new_file = await update.message.effective_attachment.get_file()
            pass

        await new_file.download_to_drive('data/input.jpeg')

        img = Image.open('data/input.jpeg')

        shape = np.array(img.size)
        shape = (shape / shape[1] * 512).astype(int)
        shape = shape // 32 * 32
        t_img = (torch.tensor(np.array(img)).permute([2, 0, 1]).unsqueeze(0) / 255.0 - 0.5)/0.25
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Detector new photo file")

        res = model.forward(t_img)    

        clone_res = res.clone()
        clone_res_cpu = clone_res.cpu()
        clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :] = torch.sigmoid(clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :])
        bboxes = decode_result(clone_res_cpu[0], threshold=0.2, iou_threshold=0.2)

        imgplot = plt.imshow(img)
        for index in range(len(bboxes['boxes'])):
            draw_box(bboxes['boxes'][index], bboxes['labels'][index])
        
        plt.savefig('data/output.jpeg')

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Detector cars")

        await context.bot.send_document(chat_id=update.effective_chat.id, document=open('data/output.jpeg', 'rb'))

        plt.clf()
        ax1.cla()
    except:
    

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Detector newFile")

        new_file = await update.message.effective_attachment.get_file()
        await new_file.download_to_drive('data/input.mp4')

        cap = cv2.VideoCapture('data/input.mp4')
        
        width, height = (
            int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter()
        output_file_name = "data/output.mp4"
        out.open(output_file_name, fourcc, fps, (width, height), True)
        
        #while cap.isOpened():
        for ff in range(40):
            ret, img = cap.read()
            
            img3 = torch.tensor(img)
            img4 = img3.permute([2,0,1]).unsqueeze(0) 

            t_img = (img4 / 255.0 - 0.5 )/0.25

            res = model.forward(t_img)    
            clone_res = res.clone()

            clone_res_cpu = clone_res.cpu()
            clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :] = torch.sigmoid(clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :])
            bboxes = decode_result(clone_res_cpu[0], threshold=0.2, iou_threshold=0.2)

            for index in range(len(bboxes['boxes'])):
                coords = bboxes['boxes'][index]
                label = bboxes['labels'][index]

                color = 'g'
                c_l = (0,255,0)
                if label == 0:
                    color = 'r'
                    c_l = (0,0,255)

                cv2.rectangle(img, (int(coords[0]), int(coords[1])), (int(coords[2]), int(coords[3])), c_l, 3)
            out.write(img)
            if not ret:
                break
            
        cap.release()
        out.release()
        cv2.destroyAllWindows()
            
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Detector cars")

        await context.bot.send_document(chat_id=update.effective_chat.id, document=open('data/output.mp4', 'rb'))


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    unknown_handler = MessageHandler(filters.ALL, unknown)
    application.add_handler(unknown_handler)
    
    application.run_polling()




