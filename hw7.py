# LOTO
import random


def shuffled_number_list():
    simple_number_list = [str(_) for _ in range(1, 91)]
    for p in range(9):
        simple_number_list[p] = str(0) + simple_number_list[p]
    random.shuffle(simple_number_list)
    return simple_number_list


def card_gen():
    work_list = shuffled_number_list()
    new_work_list = []
    b = 0
    for a in range(3):
        new_work_list.append([])
        for _ in range(5):
            x = work_list[b]
            new_work_list[a].append(x)
            b += 1
    for a in range(3):
        new_work_list[a].sort()
    players_card = []
    for a in range(3):
        players_card.append([])
        players_card[a] = [1, 1, 1, 1, 1, '  ', '  ', '  ', '  ']
        random.shuffle(players_card[a])
    for a in range(3):
        b = 0
        c = 0
        while b < 9:
            if players_card[a][b] == 1:
                players_card[a][b] = new_work_list[a][c]
                c += 1
            b += 1

    return players_card


def show_card(card, computer_card):
    print('       Карточка Игрока:\n',
          '__________________________'.ljust(0), '\n',
          ' '.join(card[0]).ljust(25), '\n',
          ' '.join(card[1]).ljust(25), '\n',
          ' '.join(card[2]).ljust(25), '\n',
          '__________________________')
    print('       Карточка Компьютера:\n',
          '__________________________'.ljust(0), '\n',
          ' '.join(computer_card[0]).ljust(25), '\n',
          ' '.join(computer_card[1]).ljust(25), '\n',
          ' '.join(computer_card[2]).ljust(25), '\n',
          '__________________________')


def remove(a, party, numbers):
    answer = 0
    for x in range(9):
        if str(numbers[a]) == party[0][x]:
            party[0][x] = (' -')
            answer += 1
        elif str(numbers[a]) == party[1][x]:
            party[1][x] = (' -')
            answer += 1
        elif str(numbers[a]) == party[2][x]:
            party[2][x] = (' -')
            answer += 1
    return answer


def numbers_to_remove():
    card = card_gen()
    computer_card = card_gen()
    temp_num = shuffled_number_list()
    a = 0
    win_points = 0
    lose_points = 0
    while a < 90:
        b = 89 - a
        answer = 0
        print(f'Новый боченок : {temp_num[a]}. (Осталось {b})\n')
        show_card(card, computer_card)
        while answer != 1 and answer != 2:
            try:
                answer = int(input('Если вы хотите удалить число - нажмите 1, иначе - 2'))
                if answer < 1:
                    print('Выберите 1 из двух вариантов!')
            except ValueError:
                print("Вы ввели неправильный символ!")
        temp_win = remove(a, card, temp_num)
        win_points = win_points + temp_win
        temp_lose = remove(a, computer_card, temp_num)
        lose_points = lose_points + temp_lose
        answer = answer + temp_win
        if answer == 1:
            print('Цифры нет на карточке. Вы проиграли!')
            break
        elif answer == 3:
            print('Цифра есть на карточке. Вы проиграли!')
            break
        print(answer)
        a += 1
        if win_points == lose_points == 15:
            print('Ничья!')
            break
        elif lose_points == 15:
            print('К сожжалению, вы проиграли! Компьютер оказался удачливее :(')
            break
        elif win_points == 15:
            print('Поздравляем! Вы победили!')
            break


numbers_to_remove()
