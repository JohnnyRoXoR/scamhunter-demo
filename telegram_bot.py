#!/usr/bin/env python3
# A basic Telegram bot for SCAMHUNTER. Requires python-telegram-bot library.

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json


def load_scammers(path: str) -> set:
    with open(path, 'r') as f:
        return set(json.load(f))


SCAMMERS = load_scammers('scammers.json')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome to SCAMHUNTER bot! Send an address to check if it's a scammer.')


async def check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    address = update.message.text.strip()
    if address in SCAMMERS:
        await update.message.reply_text(f'WARNING: {address} is flagged as a scammer!')
    else:
        await update.message.reply_text(f'{address} is not in our database.')


def main() -> None:
    import os
    token = os.getenv('TELEGRAM_TOKEN')
    if not token:
        raise EnvironmentError('Please set the TELEGRAM_TOKEN environment variable.')
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('check', check))
    application.run_polling()


if __name__ == '__main__':
    main()
