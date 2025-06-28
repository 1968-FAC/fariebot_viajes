from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = 'AQUÍ_TU_TOKEN'

async def start(update, context):
    await update.message.reply_text('¡Hola! El bot está funcionando.')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler('start', start))

app.run_polling()
