#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Создание словаря
    a = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
    # Второй словарь (будет обратным исходному)
    b = {}
    # Разделение на ключи и значения
    n = a.items()

    # Меняет местами ключи и значения
    for key, value in a.items():
        b[value] = key

    print(b)
