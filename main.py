from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("¡El bot está activo y funcionando!")

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    app.run_polling()
