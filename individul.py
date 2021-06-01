#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    dictionary=[
        {'ФИО':'Иванов И.И.', 'Номер группы':1, 'Успеваемость':4},
        {'ФИО':'Саменов С.С.', 'Номер группы':7, 'Успеваемость':2}]

def record():
        dictionary.append({
            'ФИО':input('Введите ФИО: '), 'Номер группы': int(input('Введите Номер группы: ')),
            'Успеваемость': int(input('Введите Успеваемость: '))})
        return 'Готово'

def show(s):
    di=[]
    for i in dictionary:
        if s == 2:
            if i['Успеваемость']==2: di.append(show_print(i))
        else: di.append(show_print(i))
    print(*sorted(di), sep='\n')
def show_print(d): return f"{d['ФИО']}, Номер группы: {d['Номер группы']}, Успеваемость: {d['Успеваемость']}"

while True:
    act=int(input('''
    Что Вы желаете сделать?
    1 - Записать студента в словарь
    2 - Вывести студентов имеющих оценку 2
    3 - Вывести список всех студентов
    0 - Выход из программы
    '''))
    if act == 1: print(record())
    if act == 2: show(2)
    if act == 3: show(0)
    if act == 0: break