import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import Filters, MessageHandler
import requests

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'your_bot_token' with your actual bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")  # It's a good practice to use environment variables

# Database-like structure for demonstration
users_data = {}

# Airdrop Token Amounts
INSTAGRAM_TOKEN = 1000
TWITTER_TOKEN = 800

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the Airdrop Bot! Follow the instructions to participate.")

def invite(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Share this link with your friends to invite them to the airdrop!")

def status(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_info = users_data.get(user_id, {"balance": 0})
    update.message.reply_text(f"Your current balance: {user_info['balance']} DOG tokens")

def follow_instagram(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in users_data:
        users_data[user_id] = {"balance": 0}
    users_data[user_id]['balance'] += INSTAGRAM_TOKEN
    update.message.reply_text(f"Thank you for following Instagram! You have received {INSTAGRAM_TOKEN} DOG tokens.")

def follow_twitter(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in users_data:
        users_data[user_id] = {"balance": 0}
    users_data[user_id]['balance'] += TWITTER_TOKEN
    update.message.reply_text(f"Thank you for following Twitter! You have received {TWITTER_TOKEN} DOG tokens.")

def main():
    updater = Updater(BOT_TOKEN)

    # Handlers
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('invite', invite))
    updater.dispatcher.add_handler(CommandHandler('status', status))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('follow_instagram'), follow_instagram))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('follow_twitter'), follow_twitter))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
