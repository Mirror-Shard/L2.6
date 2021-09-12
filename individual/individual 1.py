#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':

    # Список студентов.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:

        # Переменная для студента с оценкой хуже 4
        student_bad = 0

        # Средняя оценка
        average_estimation = 0

        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студенте.
            name = input("Фамилия и инициалы: ")
            group = input("Номер группы: ")

            # Ввод 5-ти оценок
            print("Введите 5 оценок через пробел:")
            evaluations = list(map(int, input().split()))

            # Проверяет количество оценок
            if len(evaluations) != 5:
                print("Неверный размер списка",)
                continue

            # Проходит по оценкам
            for i, x in enumerate(evaluations):
                # Если есть оценки кроме 4 и 5, то студент считается плохим
                if evaluations[i] == 4 or evaluations[i] == 5:
                    average_estimation += evaluations[i]
                else:
                    student_bad = 1
                    break

            # Плохой студент не заносится в список
            if student_bad:
                continue
            # Для хорошего вычисляется средняя оценка
            else:
                average_estimation /= 5

            # Создать словарь.
            student = {
                'name': name,
                'group': group,
                'average_estimation': average_estimation,
                'evaluations': evaluations,
            }

            # Добавить словарь в список.
            students.append(student)

            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda student: student['average_estimation'], reverse=True)

        elif command == 'list':

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
                    "No",
                    "Ф.И.О.",
                    "Группа",
                    "Средняя оценка"
                )
            )
            print(line)

            # Вывести данные о всех студентах.
            for idx, student in enumerate(students, 1):

                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                        student.get('average_estimation', 0)
                    )
                )
            print(line)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
            print(">>>")