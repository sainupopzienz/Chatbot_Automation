from telegram.ext import Updater, CommandHandler

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your Telegram bot.")

# Create an instance of the Updater class with your bot token
updater = Updater(token='6136893630:AAHh5KEpwZ2UABTc2OUWzNLNVDMhr3wWudo', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the start function as a handler for the /start command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()
