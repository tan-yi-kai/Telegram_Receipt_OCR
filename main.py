from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import os
from dotenv import load_dotenv, dotenv_values


## Loading variables from .env
load_dotenv()


## Function definition

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello ayyyyyy lmao")



if __name__ == '__main__':
    app = Application.builder().token(os.getenv("TOKEN")).build()
    print("Bot started")


    ## Commands
    app.add_handler(CommandHandler('start', start_command))

    ## Bot Polling
    app.run_polling(poll_interval=3)
    print("Polling")

