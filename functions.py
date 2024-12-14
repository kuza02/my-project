from random import randint
from time import sleep
from data import *


def fight(current_enemy):
    turn = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    print()
    input('Нажмите Enter, чтобы продолжить')
    print()

    while player['hp'] > 0 and enemy_hp > 0:
        if turn % 2 == 0:
            print(f'{player["name"]} атакует {enemy["name"]}')
            crit = randint(1, 100)
            if crit < player['luck']:
                enemy_hp -= player['attack'] * player['crit_multiply']
            else:
                enemy_hp -= player['attack']
            sleep(1)
            print(f'{player["name"]} - {player["hp"]}')
            print(f'{enemy["name"]} - {enemy_hp}')
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}')
            player['hp'] -= enemy['attack'] * player['armor']
            sleep(1)
            print(f'{player["name"]} - {player["hp"]}')
            print(f'{enemy["name"]} - {enemy_hp}')
            sleep(1)
        turn += 1
    if player['hp'] < 0:
        print()
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
        print()
    else:
        print()
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        print()
        current_enemy += 1
    return current_enemy


def training():
    print('1. Тренировать атаку')
    print('2. Тренировать защиту')
    print()
    action = input()
    print()
    for item in player['inventory']:
        if item['name'] == 'Пропуск тренировки':
            print('Хотите ли вы пропустить тренировку?')
            print()
            print('1. - Да')
            print('2. - Нет')
            print()
            skip = input()
            if skip == '1':
                if action == '1':
                    player['attack'] += 2
                    print(f'Ваша атака стала равна {player["attack"]}')
                elif action == '2':
                    player['armor'] -= .09
                    print(f'Ваша защита стала равна {player["armor"]}')
                player['inventory'].remove(item)
                return
            elif skip == '2':
                break
    for i in range(0, 101, 20):
        print(f'Загрузка завершина на {i}%')
        sleep(1.5)
    print('Тренировка закончена!')
    if action == '1':
        player['attack'] += 2
        print(f'Ваша атака стала равна {player["attack"]}')
    if action == '2':
        player['armor'] -= .09
        print(f'Ваша защита стала равна {player["armor"]}')
    print('')


def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атака - {player["attack"]}')
    print(f'Шанс критического урона - {player["luck"]}%')
    print(f'Множитель критического урона - x{player["crit_multiply"]}')
    resist = round((1 - player["armor"]) * 100, 1)
    print(f'Броня поглощает - {resist}% урона')


def shop():
    print(f'Приветствую, {player["name"]}. Что хочешь приобрести?')
    for key, value in items.items():
        print(f'{key}. {value["name"]} - {value["price"]}')
    print(f'''У вас сейчас {player["money"]} монет.
    ''')
    print()
    action = input()
    if items[action] in player['inventory']:
        print(f'У вас уже есть {items[action]["name"]}')
    elif player['money'] < items[action]["price"]:
        print('У вас не хватает денег!')
    else:
        print()
        print(f'Вы приобрели {items[action]["name"]}')
        player['inventory'].append(items[action])
        player['money'] -= items[action]["price"]


def display_inventory():
    print('У нас есть: ')
    for item in player['inventory']:
        print(item['name'])
    print()
    print(f'У вас сейчас {player["money"]} монет.')


def earn():
    print('Добро пожаловать в казино! У вас есть 66.66% шанс выйграть 500 монет.')
    print('А также шанс 33.33% потерять 500 монет.')
    if player['money'] < 500:
        print('У вас недостаточно монет.')
        return
    random_number = randint(1, 100)
    sleep(1.5)
    print('Результат...')
    sleep(1.5)
    print('Страшно?')
    if random_number < 67:
        print('Вы выиграли 500 монет!')
        player['money'] += 500
    else:
        print('Вы проиграли 500 монет!')
        player['money'] -= 500
    print()
    print(f'Осталось {player["money"]} монет.')

    