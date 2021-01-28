#!/usr/bin/env python

"""
Модуль генерации пароля
на основе хэширования строк
"""


import re
import hashlib


class PassGen:
    """Класс генерации паролей"""


    def __init__(self):
        self.__password = self._get_md5('')
        self.__length = 10
        self.__url = ''


    def _get_md5(self, string):
        """Хэширование строки"""

        string = str(string)
        md5 = hashlib.md5()
        md5.update(string.encode())

        return md5.hexdigest()


    def set_url(self, url):
        """Хэширование url"""

        self.__url = self._get_md5(url)


    def set_passwd(self, passwd):
        """Хэширование пароля"""

        self.__password = self._get_md5(passwd)


    def set_length(self, length):
        """Установка длины пароля"""

        try:
            self.__length = int(length)
        except ValueError:
            print("\nLength must be integer\nStandard length = 10")


    def decrypt(self):
        """Основная функция"""

        password = self.__password
        url = self.__url
        result = self._get_md5(password + url)[:self.__length]

        # Ищем числовые подстроки
        int_part = re.findall(r'([0-9]+)', result)

        # Если в пароле нет цифр или не менее 4 букв, возвращаем его
        if not int_part or len(max(int_part)) + 3 < len(result):
            return result

        new_passwd = ""
        count = 0
        sum_ = 1

        # Заменяем четные символы на буквы, если возможно
        for symbol in result:
            if sum_ < 4:
                try:
                    int_symbol = int(symbol)
                    if count%2 != 0:
                        new_passwd += chr(122 - int_symbol)
                        sum_ += 1
                        count += 1
                    else:
                        new_passwd += symbol
                        count += 1
                except ValueError:
                    new_passwd += symbol
                    count += 1
            else:
                new_passwd += symbol
                count += 1

        return new_passwd
