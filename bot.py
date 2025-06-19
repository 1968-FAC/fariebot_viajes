import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import logging

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Configurar logs
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hola, soy Fari3l Travel Bot. ¿A dónde querés viajar hoy? ✈️")

# Manejo de texto
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    await update.message.reply_text(f"📩 Recibido: {texto}")

# Ejecutar el bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()
