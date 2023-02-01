from Methods import *
from TokenBot import *
from Exceptions import *
import telebot

bot = telebot.TeleBot(TOKEN)

text_worker = Commands()


@bot.message_handler(commands=['start', 'help'])
def helping(message: telebot.types.Message):
    text = text_worker.txt_commands()
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def value(message: telebot.types.Message):
    text = text_worker.txt_values()
    for key, value_ in text_worker.txt_currency().items():
        text = '\n'.join((text, key + ' ' + value_))
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.upper().split(' ')
        if len(values) != 3:
            raise ConverterExceptions('Вы ввели некорректное значение')
        base, quote, amount = values
        if not values[2].isdigit():
            raise ConverterExceptions('Вы не ввели число')
        if base not in text_worker.txt_currency().keys() and quote not in text_worker.txt_currency().keys():
            raise ConverterExceptions('Вы ввели несуществующую валюту')
        if base == quote:
            raise ConverterExceptions(f'Нельзя переводить одинаковые валюты "{quote}"')
        conversion_result = Method.get_price(base=base,
                                             quote=quote,
                                             amount=amount)
    except ConverterExceptions as error:
        bot.send_message(message.chat.id, f'\n{error}')
    else:
        text = f'Цена {amount} {base} в {quote} - {round(conversion_result)}'
        bot.send_message(message.chat.id, text)


bot.polling()
