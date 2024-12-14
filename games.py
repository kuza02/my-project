from data import *
from functions import *

name = input('Введи свое имя, путник: ')
player['name'] = name
current_enemy = 0

while True:
    print()
    print('Выберите действие: ')
    print('1. Сражение')
    print('2. Тренировка')
    print('3. Информация об игроке')
    print('4. Магазин')
    print('5. Инвентарь')
    print('6. Заработок')
    print()
    action = input()
    print()
    if action == '1':
        current_enemy = fight(current_enemy)
    elif action == '2':
        training()
    elif action == '3':
        display_player()
    elif action == '4':
        shop()
    elif action == '5':
        display_inventory()
    elif action == '6':
        earn()
    
    