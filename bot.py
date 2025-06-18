import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Definir comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot de viajes ✈🌍. ¿En qué puedo ayudarte?")

# Configurar y ejecutar el bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
