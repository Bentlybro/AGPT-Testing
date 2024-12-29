from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging
from config import TELEGRAM_BOT_TOKEN

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the !hello command"""
    try:
        # Get the message text and user information
        message = update.message
        user = message.from_user.first_name

        # Check if the message starts with !hello
        if message.text.lower().startswith('!hello'):
            await message.reply_text(f"Hello {user}")
    except Exception as e:
        logger.error(f"Error in hello_command: {str(e)}")
        await message.reply_text("Sorry, something went wrong!")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Start the bot"""
    # Create the Application instance
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello_command))
    
    # Add error handler
    application.add_error_handler(error_handler)

    # Start the bot
    application.run_polling(poll_interval=1)
    
if __name__ == '__main__':
    main()