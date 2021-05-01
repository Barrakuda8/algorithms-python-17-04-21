"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

from hashlib import sha256
from uuid import uuid4


class UrlCash:

    cash = {}
    salts = []

    def __init__(self, url):
        self.salt = uuid4().hex
        self.salts.append(self.salt)
        self.url = sha256(self.salt.encode() + url.encode()).hexdigest()
        self.cash[self.url] = url


def cash_check():
    url = input('Введите url: ')  # для удобства тестирования
    for salt in UrlCash.salts:
        if sha256(salt.encode() + url.encode()).hexdigest() in UrlCash.cash:
            return
    UrlCash(url)
    #print(UrlCash.cash)


cash_check()
#cash_check()
#cash_check()
#cash_check()
#cash_check()