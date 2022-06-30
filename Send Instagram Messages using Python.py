# pip install instabot

from instabot import Bot
bot = Bot()

bot.login(username="Your Username", password="Your Password")
bot.send_message("Hi Brother", ["Receiver's Username"])