#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

#a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше
# положенного или больше чем имеется в куче.
#b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет,
# то он, однозначно, проиграет. Достаточно довести игру до такой ситуации.

table_amount = 2021


def bot_play(table_amount):
    player_num = 1
    table_amount = table_amount
    player_amount = 0

    while table_amount != 0:
        if player_num == 1:
            print('!!!Ваш ход!!!')
            print('Кол-во конфет на столе:', table_amount)
            print('Кол-во конфет у противника:', player_amount)
            print('#########################################')
            amount = int(input('Введите кол-во забираемых конфет: '))
            print('#########################################')

            if amount > table_amount:
                print('Низя брать больше чем лежит на столе!')
                continue
            elif amount > 28:
                print('Низя брать больше 28!')
                continue
            table_amount -= amount
            player_amount += amount
            if player_num == 1:
                player_num = 2
            else:
                player_num = 1
        else:
            if table_amount >= 85:
                amount = random.randint(1, 28)
            elif table_amount > 57:
                amount = random.randint(1, table_amount - 57)
            elif table_amount > 29:
                amount = table_amount - 29
            elif table_amount == 29:
                amount = 1
            else:
                amount = table_amount

            table_amount -= amount
            player_amount += amount
            print('Бот взял ' + str(amount) + ' конфет')
            print('#########################################')
            if player_num == 1:
                player_num = 2
            else:
                player_num = 1

    if player_num == 1:
        print('Победа! Победитель: Бот')
    else:
        print('Победа! Победитель: Игрок')


def pvp_play(table_amount):
    player_num = 1
    table_amount = table_amount
    player_amount = 0

    while table_amount != 0:

        print('!!!Ход игрока №' + str(player_num) + '!!!')
        print('Кол-во конфет на столе', table_amount)
        print('Кол-во конфет у противника', player_amount)
        print('#########################################')
        amount = int(input('Введите кол-во забираемых конфет: '))
        print('#########################################')

        if amount > table_amount:
            print('Низя брать больше чем лежит на столе!')
            continue
        elif amount > 28:
            print('Низя брать больше 28!')
            continue
        table_amount -= amount
        player_amount += amount
        if player_num == 1:
            player_num = 2
        else:
            player_num = 1

    if player_num == 1:
        player_num = 2
    else:
        player_num = 1
    print('Победа! Победитель: Игрок №' + str(player_num))


with_bot = None
answer = input('Играть с ботом? (Да или нет): ').lower()
if answer == 'да':
    with_bot = True
elif answer == 'нет':
    with_bot = False
print(with_bot)

if with_bot is not None:
    if with_bot:
        bot_play(table_amount)
    else:
        pvp_play(table_amount)









