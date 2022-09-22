# Создайте программу для игры в ""Крестики-нолики"".
# Пример интерфейса:
#
#    |   | 0
# -----------
#    |   |
# -----------
#    | X |
# Ввод можно реализовать через введение двух чисел (номеров строки и столбца).

def write_field(field):
    for row in field:
        row1 = ''
        for symbol in row:
            row1 += symbol + '|'
        row1 = row1[:len(row1) - 1]
        print(row1)


def draw_check(field):
    set = []
    draw = False
    for row in field:
        for symbol in row:
            set.append(symbol)
    if ' ' not in set:
        draw = True
    return draw


def win_check(field):
    win = False
    # проверка по линиям
    for row in field:
        if len(set(row)) == 1 and ' ' not in row:
            win = True
            print('Победитель1: ', set(row))
            # проверка по рядам
    column1 = []
    column2 = []
    column3 = []
    for row in field:
        column1.append(row[0])
        column2.append(row[1])
        column3.append(row[2])
    if len(set(column1)) == 1 and ' ' not in column1:
        win = True
        print('Победитель2: ', set(column1))
    if len(set(column2)) == 1 and ' ' not in column2:
        win = True
        print('Победитель3: ', set(column2))
    if len(set(column3)) == 1 and ' ' not in column3:
        win = True
        print('Победитель4: ', set(column3))
        # проверка по диагоналям
    diagonal1 = [field[0][0], field[1][1], field[2][2]]
    diagonal2 = [field[0][2], field[1][1], field[2][0]]
    if len(set(diagonal1)) == 1 and ' ' not in diagonal1:
        win = True
        print('Победитель5: ', set(diagonal1))
    if len(set(diagonal2)) == 1 and ' ' not in diagonal2:
        win = True
        print('Победитель6: ', set(diagonal2))
    return win


field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
symbol = 'o'

while win_check(field) == False:
    if draw_check(field):
        print('Ничья!')
        break
    choice = input('Введите 2 числа(<строка>,<ряд>)(пример: 1,2): ')
    choice1 = choice.split(',')
    pos1 = int(choice1[0])
    pos2 = int(choice1[1])
    if field[pos1 - 1][pos2 - 1] == ' ':
        field[pos1 - 1][pos2 - 1] = symbol
        if symbol == 'o':
            symbol = 'x'
        else:
            symbol = 'o'
    else:
        print('Поле занято!')
        continue
    write_field(field)