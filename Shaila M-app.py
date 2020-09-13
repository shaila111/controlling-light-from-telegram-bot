!pip install adafruit-io

import os

x = os.getenv('x')
y = os.getenv('y')

from Adafruit_IO import Client, Feed
aio = Client(x,y)

feed = Feed(name='bot')

result = aio.create_feed(feed)

result

from Adafruit_IO import Data

!pip install python-telegram-bot

from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler

def on(bot,update):
  chat_id = update.message.chat_id    
  aio.create_data('bot',Data(value = 1))
  bot.send_message(chat_id =chat_id,text ="Lights On")
  
 def off(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('bot',Data(value = 0))
  bot.send_message(chat_id =chat_id,text ="Lights Off")
  
updater = Updater('1175375675:AAGHG1X2YTQaNm28DXW5OPaaIwuT-TIYSiE')
dp = updater.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
updater.start_polling()
updater.idle()
