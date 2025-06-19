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

# Cargar variables desde .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✈️ Hola, soy tu asistente de viajes. ¿A dónde te gustaría ir hoy?")

# Manejo de texto libre
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    await update.message.reply_text(f"Recibido: {texto}")

# Arranque de la aplicación
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()
