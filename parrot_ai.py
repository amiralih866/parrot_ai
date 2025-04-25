import datetime

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
from main import ai as parrot

TELEGRAM_BOT_TOKEN = ("7850863295:AAHZa5ZmSRAWa8br-IoXuFQ23S3P6BcW_9w")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am parrot bot 🤖 \n write: chat 'YOUR_MESSAGE'")


app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()


async def chat_with_parrot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    if message.startswith('chat '):
        await update.message.reply_text('Thinking...')
        if message.find('clock'):
            await update.message.reply_text(str(datetime.datetime.now()).split(' ')[1].split('.')[0])
        else:
            reply = str(update.message).lower().split('chat ')[1]
            await update.message.reply_text(str(parrot(reply)))
    elif message.startswith('چت '):
        await update.message.reply_text('Thinking...')
        if message.find('ساعت'):
            await update.message.reply_text(str(datetime.datetime.now()).split(' ')[1].split('.')[0])
        else:
            reply = str(update.message).lower().split('چت ')[1]
            await update.message.reply_text(str(parrot(reply)))


app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), chat_with_parrot))
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
