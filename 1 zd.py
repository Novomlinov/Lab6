#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    school = {'1а': 26, '1б': 20, '2а': 10, '6а': 23, '7в': 24, '8а': 17, '9б': 18}
    while True:
        print('change - Изменилось количество учеников:')
        print('add - В школе появился новый класс')
        print('remove - В школе был расформирован (удален) класс')
        print('list - Выгрузка данных')
        print('all - Общее число учащихся в школе')
        print('end - Выход')
        n = input('Введите название операции >>> ')
        if n == 'change':
            school.update({input(f'Название изменяемого класса: '):
                        int(input(f'Количество учеников изменяемого класса: '))})
        elif n == 'add':
            school.update({input(f'Название класса №: '): int(input(f'Количество учеников класса №: '))})
        elif n == 'remove':
            del school[input(f'Название расформировываемого класса: ')]
        elif n == 'list':
            print(school)
        elif n == 'all':
            print(sum(school.values()))
        elif n == 'end':
            break