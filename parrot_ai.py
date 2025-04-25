import datetime

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
from main import ai as parrot

TELEGRAM_BOT_TOKEN = ("7850863295:AAHZa5ZmSRAWa8br-IoXuFQ23S3P6BcW_9w")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    سلام به همه من ربات طوطی هستم که از هوش مصنوعی قدرت گرفته ام🦜🫡
    فعلا به علت مشغله زیاد قابلیت های زیادی ندارم
    مزیت من نسبت به ربات های دیگر اضافه شدن به گروه و پاسخ به اعضا است
    .
    شما میتوانید به راحتی من را به گروه خود اضافه کنید و با من مکالمه کنید
    برای مکالمه کافیه بنویسید:
    چت + "متن پیام مورد نظر خودتون"
    تا من پاسخ شما رو همونجا بدم

    اگر هم قابلیت های من رو فراموشی کردی میتونی دستور /start رو بزنی
    """)


app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()


async def chat_with_parrot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    if message.startswith('chat '):
        await update.message.reply_text('Thinking...')
        reply = str(update.message).lower().split('chat ')[1]
        await update.message.reply_text(str(parrot(reply)))
    elif message.startswith('چت '):
        await update.message.reply_text('Thinking...')
        reply = str(update.message).lower().split('چت ')[1]
        await update.message.reply_text(str(parrot(reply)))


app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), chat_with_parrot))
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
