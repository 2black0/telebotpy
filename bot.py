from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def start(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    print(chat_id)

def main():
    print('CTRL+Z for Exit')
    updater = Updater('830581916:AAHftjziRPbuPgPmDIa_mYQvNHwnVl7WMk4')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()