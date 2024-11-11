import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers import start_handler, check_handler,  help_handler, button_handler, message_handler
from config import TOKEN

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start_handler)) # start handler
    application.add_handler(CommandHandler("help", help_handler))  # help handler
    application.add_handler(CallbackQueryHandler(button_handler))  # handler untuk button
    application.add_handler(CommandHandler("cek", check_handler)) # cek handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)) # "Bagaimana cara menggunakan bot ini?" handle

    # Running bot
    application.run_polling()

if __name__ == "__main__":
    main()
