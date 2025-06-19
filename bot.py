import logging
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from dotenv import load_dotenv

# Carga el token desde .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Configura el registro
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy tu asistente de viajes. ¿En qué puedo ayudarte?")

# Respuesta a texto libre
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_usuario = update.message.text
    respuesta = f"Recibido: {texto_usuario}"
    await update.message.reply_text(respuesta)

# Main app
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()
