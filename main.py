from telegram.ext import ApplicationBuilder, CommandHandler
import os

# Obtener el token desde las variables de entorno
TOKEN = os.getenv("BOT_TOKEN")

# Crear la aplicación
app = ApplicationBuilder().token(TOKEN).build()

# Definir el comando /start
async def start(update, context):
    await update.message.reply_text('¡Hola! El bot está funcionando correctamente.')

# Añadir el handler
app.add_handler(CommandHandler('start', start))

# Ejecutar el bot
if __name__ == '__main__':
    app.run_polling()
