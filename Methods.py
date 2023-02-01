import requests
import json
from Exceptions import *


class Commands:
    def __init__(self):
        self.commands_text = None
        self.values_text = None
        self.currency_text = None

    def txt_commands(self):
        self.commands_text = 'Что бы воспользоваться ботом:\n\n|Введите валюту которую хотите конвертировать|\n\
|Валюту в которую будете конвертировать|\n\
|Кол-во конвертируемой валюты|\n\
|Список доступных валют:  /values|\n\
|Пример ввода: USD EUR 100'
        return self.commands_text

    def txt_values(self):
        self.values_text = 'Доступные валюты:'
        return self.values_text

    def txt_currency(self):
        self.currency_text = {'USD': 'Доллар',
                              'RUB': 'Рубль',
                              'EUR': 'Евро',
                              'BYN': 'Белорусский Рубль',
                              'KZT': 'Казахстанский тенге',
                              'UAH': 'Украинская гривна',
                              'AMD': 'Армянский драм'}

        return self.currency_text


class Method:

    @staticmethod
    def get_price(base, quote, amount):
        try:
            request = requests.get(
                f'https://v6.exchangerate-api.com/v6/36044686ed4ea0bba53d6ff5/pair/{base}/{quote}/{amount}')
            if json.loads(request.content)["result"] == 'error':
                raise ConverterExceptions('Ошибка на сервере')
            else:
                return json.loads(request.content)['conversion_result']
        except requests.exceptions.ConnectionError:
            raise ConverterExceptions('Ошибка подключения')
