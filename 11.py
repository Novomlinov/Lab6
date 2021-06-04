#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys


if __name__ == '__main__':
    students = []
    while True:
        command = input(">>> ").lower()
        if command == '0':
            break
        elif command == '1':
            name = input("Фамилия и инициалы ")
            post = input("Номер группы ")
            a = int(input("Русский язык "))
            b = int(input("Математика "))
            c = int(input("Информатика "))
            d = int(input("История "))
            e = int(input("Физика "))
            student = {
            'name': name,
            'post': post,
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'e': e,
            }
            students.append(student)
            if len(students) > 1:
                students.sort(key=lambda item: item.get('name', ''))
        elif command == '2':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
            )
            print(line)
            print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "№",
            "Ф.И.О.","Должность",
            "Год" ))
            print(line)
            for idx, student in enumerate(students, 1):
                print("ФИО:", student.get('name', ''), "Номер группы:", student.get('post', ''), "Русский язык:", student.get('a', 0),
                      "Математика:", student.get('b', 0), "Информатика:", student.get('c', 0),
                      "История:", student.get('d', 0), "Физика:", student.get('e', 0))
        elif command == '3':
            count = 0
            for student in students:
                if (student.get('a') <= 2) or (student.get('b') <= 2) or (student.get('c') <= 2)\
                        or (student.get('d') <= 2) or (student.get('e') <= 2):
                    count += 1
                    print('{:>4}: {}'.format(count, student.get('name', '')))
            if count == 0:
                print("Таких студентов не выявлено.")
        elif command == 'help':
            print("Список команд:\n")
            print("1 - Добавить студента;")
            print("2 - Список студентов;")
            print("3 - Студенты с плохой успеваемостью;")
            print("help - отобразить справку;")
            print("0 - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)