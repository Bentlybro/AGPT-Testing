import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Command handler for /hello
async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the username of the person who sent the command
    username = update.effective_user.first_name
    # Send the response
    await update.message.reply_text(f"Hello {username}")

async def main():
    # Initialize the bot with your token
    app = Application.builder().token("YOUR_BOT_TOKEN_HERE").build()

    # Add command handler
    app.add_handler(CommandHandler("hello", hello_command))

    # Start the bot
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())