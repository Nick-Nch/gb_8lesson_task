# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

import random

class Card:
    def __init__(self, lenght=90):
        self.first = [x for x in range(1, lenght + 1)]
        self.fifteen = []
        self.point = 15
        self.get_15_items()
        self.orig_line = [x for x in range(9)]
        self.lines = self.random_sort(self.orig_line.copy())


    def get_15_items(self):
        try:
            five = []
            copy_list = self.first.copy()
            for x in range(1, 4):
                for y in range(1, 6):
                    i = random.randrange(0, len(copy_list))
                    five.append(copy_list[i])
                    copy_list.pop(i)
                five.sort()
                self.fifteen.append(five.copy())
                five.clear()
            return self.fifteen
        except ValueError:
            return 'list is smaller'

    def random_sort(self, first):
        lines = []
        for x in range(3):
            for y in range(10):
                x1 = random.randint(0, 8)
                x2 = random.randint(0, 8)
                if x1 != x2:
                    first[x1], first[x2] = first[x2], first[x1]
            lines.append(first.copy())
        return lines

    def check_out(self):
        pass

    def create_card(self):
        print('...................................')
        for x in range(3):
            line = ''
            y = 0
            for i, el in enumerate(self.lines[x]):
                if el == 5 or el == 6 or el == 7 or el == 8:
                    line += ''.rjust(2)
                else:
                    line += str(self.fifteen[x][y]).rjust(2)
                    y += 1
                if i < len(self.lines[x]) - 1:
                    line += ''.rjust(2)
            print(line)
        print('...................................')

card = Card()

print(card.create_card())





