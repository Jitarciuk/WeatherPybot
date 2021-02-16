# This is a sample Python script.


from pyowm import OWM
import telebot
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('479e975ab63b4afe463ef20d50924fae', config_dict)


bot = telebot.TeleBot("1633823040:AAH8WuWGaJ7ipgrAyTjWgiABjSw_sViGAhI")


@bot.message_handler(content_types=['text'])
def send_weather(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас в районе :" + str(w.temperature('celsius')["temp"]) + "\n"
    bot.send_message(message.chat.id,answer)

bot.polling( none_stop = True)
