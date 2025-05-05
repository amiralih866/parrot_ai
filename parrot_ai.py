import telegram.error
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
from main import ai as parrot

TELEGRAM_BOT_TOKEN = "7850863295:AAHZa5ZmSRAWa8br-IoXuFQ23S3P6BcW_9w"
TEST_BOT_TOKEN = "7940159413:AAHwcDpIqx2oychT7DvtUjRNzbwRgCXy9Ao"


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
    try:
        message = str(update.message.text)

        if message.startswith('چت '):
            await update.message.reply_text('بذار یکم فکر کنم🤔...')
            reply = str(update.message.text).split('چت ', 1)[1]

            try:
                print('asked ' + reply + ':')
                chat_reply = parrot(reply)

                # Try to send response with Markdown
                try:
                    await update.message.reply_text(text=chat_reply, parse_mode=ParseMode.MARKDOWN)
                except telegram.error.BadRequest:
                    # If Markdown parsing fails, send without formatting
                    await update.message.reply_text(text=chat_reply, parse_mode=None)

                print("Chat replied: " + chat_reply)
            except Exception as e:
                error_message = f"در کنکاش پیامت به این مشکل برخوردم ببین میفهمی چی میگه🤷🏻‍♂️؟: {str(e)}"
                await update.message.reply_text(error_message)
                print(f"ERROR: {error_message}")

    except AttributeError:
        await update.message.reply_text("متاسفانه در پردازش پیام شما دچار مشکل شدم، دوباره تلاش کنید 😁")
    except Exception as e:
        print(f"Unhandled error: {str(e)}")
        try:
            await update.message.reply_text("سرم گیج رفته نمیفهمم چی میگی")
        except:
            print("Could not send error message to user")


app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), chat_with_parrot))
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
