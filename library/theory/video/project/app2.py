import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = '5973353632:AAFCatfGzjItHliXgPe9ybY3RDmOL-Er0sk'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

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
    print('---1----')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Detector newFile")

    #await context.bot.send_document(chat_id=update.effective_chat.id, document=open('data/output11.mp4', 'rb'))

    #newFile = update.message.effective_attachment.get_file()
    #newFile.download('data/output11q.mp4')



    new_file = await update.message.effective_attachment.get_file()
    await new_file.download_to_drive('data/file_name_11')

    #context.bot.get_file(update.message.document).download()

    # writing to a custom file
    #with open("data/file21.doc", 'wb') as f:
    #    #f.write('222')
    #    context.bot.get_file(update.message.document).download(out=f)


    await context.bot.send_message(chat_id=update.effective_chat.id, text="Detector cars")




if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    unknown_handler = MessageHandler(filters.ALL, unknown)
    application.add_handler(unknown_handler)
    
    application.run_polling()
