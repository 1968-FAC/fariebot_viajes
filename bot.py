from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)
import os

# Obtener el token desde la variable de entorno
TOKEN = os.getenv("BOT_TOKEN")

# Definir el manejador para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Bienvenido a Fari3l Travel Bot. 🚀")

# Crear la aplicación del bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Agregar el manejador de comando
    app.add_handler(CommandHandler("start", start))

    # Ejecutar el bot
    app.run_polling()

if __name__ == '__main__':
    main()
