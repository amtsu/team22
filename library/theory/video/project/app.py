from flask import Flask
#from redis import Redis


import torch
import pytorch_lightning as pl
import torchvision

#from PIL import Image

#import numpy as np

#import time

#import matplotlib.pyplot as plt

#from torch import nn
#import cv2

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



app = Flask(__name__)
#redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    
#    device = 'cpu:0'
    device = 'cpu'
    
    state = torch.load(
    
        #'/content/drive/MyDrive/DS/Video/hw5/file/weights/detector_checkpoint.ckpt',
        'data/detector_checkpoint.ckpt',
        map_location='cpu')
    state = state['state_dict']

    model = PLModel(RetinaRehead())
    model.load_state_dict(state)

    #model = model.model.to(device).eval()
    #model = model.model.to(device).eval().half()
    #model = model.model.eval()#.half()
    model = model.model.to(device).eval()
    #model = model.model.eval()

    ##

    mm = model.forward(torch.rand(1, 3, 512, 512).to(device))  #warm up
    #_ = model.forward(torch.rand(1, 3, 512, 512).half().to(device))  #warm up
##    _ = model.forward(torch.rand(1, 3, 512, 512).half())  #warm up
    #_ = model.forward(torch.rand((1, 3, 512, 512), dtype=torch.half).to(device))  #warm up
##    
    #_ = model.forward(torch.rand(1, 3, 512, 512))  #warm up
    print(mm.shape)
    
    ##
    
    #img = Image.open('/content/drive/MyDrive/DS/Video/hw5/file/test_images_videos/photo1681218949.jpeg')
    img = Image.open('data/photo1681218949.jpeg')
    #img = Image.open('/content/drive/MyDrive/DS/Video/hw5/file/test_images_videos/photo1681218949.jpeg')
    shape = np.array(img.size)
    shape = (shape / shape[1] * 512).astype(int)
    #shape = (shape / shape[1] * 512).astype(torch.half)
    shape = shape // 32 * 32

    ##
    
    print(shape)
    
    ##

    t_img = (torch.tensor(np.array(img)).permute([2, 0, 1]).unsqueeze(0) / 255.0 - 0.5)/0.25
    
#    times_for_preproc = []
#
#    for i in range(2):
#      #torch.cuda.synchronize(device=device)
#      t0 = time.time()
#
#      img = img.resize(size=shape)
#      t_img = (torch.tensor(np.array(img)).permute([2, 0, 1]).unsqueeze(0) / 255.0 - 0.5)/0.25
#      #t_img = t_img.to(device)
##      t_img = t_img.to(device)#.half()
#
#      #torch.cuda.synchronize(device=device)
#      times_for_preproc.append(time.time() - t0)
#
#    print(f'mean time for preprocessing {np.mean(np.array(times_for_preproc))}')

    ##
    
    t_img.shape
    
    ##

    res = model.forward(t_img)    

#    times_for_inf_torch = []
#
#    for i in range(2):
#      #torch.cuda.synchronize(device=device)
#      t0 = time.time()
#
#      res = model.forward(t_img)
#      #res = model.forward(t_img.half())
#
#      #torch.cuda.synchronize(device=device)
#      times_for_inf_torch.append(time.time() - t0)
#
#    print(f'mean time for inference torch {np.mean(np.array(times_for_inf_torch))}')

    ##


    ##
    
    #clone_res = res.clone().detach()
    clone_res = res.clone()
    
    ##
    
    clone_res_cpu = clone_res.cpu()
    clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :] = torch.sigmoid(clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :])
    bboxes = decode_result(clone_res_cpu[0], threshold=0.2, iou_threshold=0.2)

#    times_for_postproc = []
#
#    #for i in range(100):
#    for i in range(2):
#      #torch.cuda.synchronize(device=device)
#      t0 = time.time()
#
#      clone_res_cpu = clone_res.cpu()
#      #clone_res_cpu = clone_res.to(dtype=torch.float16)#.cpu()
#      #clone_res_cpu = clone_res.to(dtype=torch.float32).cpu()
#      #clone_res_cpu = clone_res.cpu()
##      clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :] = torch.sigmoid(clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, #:])
#      clone_res_cpu[:, [1, 2, 6, 7 ], :, :] = torch.sigmoid(clone_res_cpu[:, [1, 2, 6, 7], :, :])
#      #clone_res[:, [0, 1, 2, 5, 6, 7], :, :] = torch.sigmoid(clone_res[:, [0, 1, 2, 5, 6, 7], :, :])
#      #clone_res_cpu = clone_res.cpu()
#      bboxes = decode_result(clone_res_cpu[0], threshold=0.2, iou_threshold=0.2)
#
#      #torch.cuda.synchronize(device=device)
#      times_for_postproc.append(time.time() - t0)
#
#    print(f'mean time for postprocessing {np.mean(np.array(times_for_postproc))}')

    ##
    
    
    #plt.imshow(img)
    imgplot = plt.imshow(img)
    for index in range(len(bboxes['boxes'])):
        draw_box(bboxes['boxes'][index], bboxes['labels'][index])
    
    ##
    
    #imgplot = plt.imshow(img)
    
    plt.savefig('data/test4.jpeg')
    
    #plt.imsave('data/test1.jpeg', imgplot)
    
    
    #redis.incr('hits')
    #print(torch.cuda.get_device_name(0))
    print(torch.cuda)
    #return 'This Compose/Flask demo has been viewed %s time(s). %s' % redis.get('hits'), torch.cuda.get_device_name(0)
    #return (torch.cuda, shape, t_img.shape)
    #return 'This Compose/Flask demo. %s - %s - %s' % (torch.cuda, shape, t_img.shape)
    return  f"""
        test: {torch.cuda} == {shape} == {t_img.shape} <br>
        clone_res_cpu {clone_res_cpu.size()}<br>
        bboxes {bboxes}<br>
        bboxes['boxes'] {bboxes['boxes'].size()}<br>
        bboxes['labels'] {bboxes['labels'].size()}<br>
        bboxes['scores'] {bboxes['scores'].size()}<br>
        mm.shape {mm.shape}<br>
        
        """

    return  f"""
        test: {torch.cuda} == {shape} == {t_img.shape} <br>
        mean time for preprocessing {np.mean(np.array(times_for_preproc))}<br>
        mean time for inference torch {np.mean(np.array(times_for_inf_torch))}<br>
        mean time for postprocessing {np.mean(np.array(times_for_postproc))}<br>
        clone_res_cpu {clone_res_cpu.size()}<br>
        bboxes {bboxes}<br>
        bboxes['boxes'] {bboxes['boxes'].size()}<br>
        bboxes['labels'] {bboxes['labels'].size()}<br>
        bboxes['scores'] {bboxes['scores'].size()}<br>
        mm.shape {mm.shape}<br>
        
        """
# %  torch.cuda.get_device_name(0)
    #return 'This Compose/Flask demo has been viewed time(s)'# % redis.get('hits')


import cv2
    
@app.route('/video')
def video():
    cap = cv2.VideoCapture('data/driving_out_30sec.mp4')
    
    times_to_grab_images = []
    while cap.isOpened():
      t0 = time.time()
      ret, image_np = cap.read()
      times_to_grab_images.append(time.time() - t0)

      if not ret:
        break

    print(f'mean time for grab image: {np.mean(np.array(times_to_grab_images))}')
    
    return  f"""
        mean time for grab image: {np.mean(np.array(times_to_grab_images))}  <br>
        
        cv2.getBuildInformation() = {cv2.getBuildInformation()}<br>
        
        """

@app.route('/video1')
def video1():

    device = 'cpu'    
    state = torch.load(
        'data/detector_checkpoint.ckpt',
        map_location='cpu')
    state = state['state_dict']

    model = PLModel(RetinaRehead())
    model.load_state_dict(state)
    model = model.model.to(device).eval()
    
    
    cap = cv2.VideoCapture('data/driving_out_30sec.mp4')
    for i in range(30*25):
        ret, img = cap.read()
    
    #img2 = Image.open('data/photo1681218949.jpeg')
    #shape = np.array(img2.size)
    
    img3 = torch.tensor(img)
    img4 = img3.permute([2,0,1]).unsqueeze(0) 

    #shape = (shape / shape[1] * 512).astype(int)
    #shape = shape // 32 * 32
    #t_img = (torch.tensor(np.array(img)).permute([2, 0, 1]).unsqueeze(0) / 255.0 - 0.5)/0.25
       
     #images = self.data.iloc[idx, 1:-1].values.astype(np.uint8).reshape((1, 16, 16))
        
#    return  f"""
#        ret: {ret}<br>
#        img {img3.size()}<br>
#        img2 {shape}<br>
#        t_img {t_img.size()}<br>
#        img4 {img4.size()}<br>
#        """         
         
    t_img = (img4 / 255.0 - 0.5 )/0.25
    

    res = model.forward(t_img)    
    clone_res = res.clone()
    
    clone_res_cpu = clone_res.cpu()
    clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :] = torch.sigmoid(clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :])
    bboxes = decode_result(clone_res_cpu[0], threshold=0.2, iou_threshold=0.2)


    imgplot = plt.imshow(img)
    for index in range(len(bboxes['boxes'])):
        draw_box(bboxes['boxes'][index], bboxes['labels'][index])
    
    plt.savefig('data/test5.jpeg')

#            img2 {shape}<br>
#        test: {torch.cuda} == {shape} == {t_img.shape} <br>

    return  f"""
        ret: {ret}<br>
        img {img3.size()}<br>
        t_img {t_img.size()}<br>
        img4 {img4.size()}<br>
        <br>

        clone_res_cpu {clone_res_cpu.size()}<br>
        bboxes {bboxes}<br>
        bboxes['boxes'] {bboxes['boxes'].size()}<br>
        bboxes['labels'] {bboxes['labels'].size()}<br>
        bboxes['scores'] {bboxes['scores'].size()}<br>
        
        
        """





@app.route('/video2')
def video2():

    device = 'cpu'    
    state = torch.load(
        'data/detector_checkpoint.ckpt',
        map_location='cpu')
    state = state['state_dict']

    model = PLModel(RetinaRehead())
    model.load_state_dict(state)
    model = model.model.to(device).eval()
    
    cap = cv2.VideoCapture('data/driving_out_30sec.mp4')
    
    
    ##cap = cv2.VideoCapture(0)
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('data/output.avi', fourcc, 20.0, (640, 480))

    width, height = (
        int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    )
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter()
    output_file_name = "data/output3.mp4"
    out.open(output_file_name, fourcc, fps, (width, height), True)

    
    #while cap.isOpened():
    for ff in range(200):
        print(1)
        ret, img = cap.read()
        
        img3 = torch.tensor(img)
        img4 = img3.permute([2,0,1]).unsqueeze(0) 


        t_img = (img4 / 255.0 - 0.5 )/0.25


        res = model.forward(t_img)    
        clone_res = res.clone()

        clone_res_cpu = clone_res.cpu()
        clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :] = torch.sigmoid(clone_res_cpu[:, [0, 1, 2, 5, 6, 7], :, :])
        bboxes = decode_result(clone_res_cpu[0], threshold=0.2, iou_threshold=0.2)

        #imgplot = plt.imshow(img)
        
        for index in range(len(bboxes['boxes'])):
            #draw_box(bboxes['boxes'][index], bboxes['labels'][index])

            coords = bboxes['boxes'][index]
            label = bboxes['labels'][index]

            #x = np.array((coords[0], coords[2]))
            #y = np.array((coords[1], coords[3]))
            color = 'g'
            c_l = (0,255,0)
            if label == 0:
                color = 'r'
                c_l = (0,0,255)


            #plt.plot(x.mean(), y.mean(), '*' + color)

            #plt.plot([x[0], x[0]], [y[0], y[1]], color)
            #plt.plot([x[1], x[1]], [y[0], y[1]], color)
            #plt.plot([x[0], x[1]], [y[0], y[0]], color)
            #plt.plot([x[0], x[1]], [y[1], y[1]], color)
            
            #return  f"""
            #{coords[0]}
            #"""
            
            #cv2.rectangle(img, (coords[0], coords[2]), (coords[1], coords[3]), (0, 255, 0), 3)
            #cv2.rectangle(img, (int(coords[0]), int(coords[2])), (int(coords[1]), int(coords[3])), (0, 255, 0), 3)
            cv2.rectangle(img, (int(coords[0]), int(coords[1])), (int(coords[2]), int(coords[3])), c_l, 3)

            
        #return  f"""
        #    imgplot: {imgplot}<br>
        #    """
        
        #plt.savefig('data/test5.jpeg')
    
        #ret, frame = cap.read()
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(img)

        print(2)
    
        if not ret:
            break

        
    cap.release()
    out.release()
    cv2.destroyAllWindows()
        

    
    




#            img2 {shape}<br>
#        test: {torch.cuda} == {shape} == {t_img.shape} <br>

    return  f"""
        ret: {ret}<br>
        img {img3.size()}<br>
        t_img {t_img.size()}<br>
        img4 {img4.size()}<br>
        <br>

        clone_res_cpu {clone_res_cpu.size()}<br>
        bboxes {bboxes}<br>
        bboxes['boxes'] {bboxes['boxes'].size()}<br>
        bboxes['labels'] {bboxes['labels'].size()}<br>
        bboxes['scores'] {bboxes['scores'].size()}<br>
        
        
        """


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
