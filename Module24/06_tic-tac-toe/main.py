import os


class Cell:
    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    def __init__(self, number, empty):
        self.number = number
        self.empty = empty

    def empty_status(self):  # показывает пустая клетка или нет
        if self.empty == '   ':
            return True
        else:
            return False


class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        self.board = [Cell(i, '{:^3}'.format(' ')) for i in range(1, 10)]

    def display(self):  # Рисует поле с содержимым клеток
        count = 0
        for cell in self.board:
            if count == 3:
                print()
                count = 0
            print('|', cell.number, cell.empty, '|', end=' ')
            count += 1
        print('\n')


class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
    def __init__(self, name, figure):
        self.name = name
        self.figure = '{:^3}'.format(figure)


class Game:
    # словарь статуса игры
    game_state_dict = {1: 'Начало игры', 2: 'Идет игра', 3: 'Game over', 4: 'Ничья'}
    vin_list = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]]

    # класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    # А также методы:
    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.
    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.
    def __init__(self, player_1, player_2, board=Board(), state=1):
        self.name_1 = player_1
        self.name_2 = player_2
        if isinstance(board, Board):
            self.board_value = board
            self.players = [Player(self.name_1, 'X'), Player(self.name_2, 'O')]
        else:
            print('неверно передал аргумент')
        self.game_state = state
        self.score = {self.name_1: 0, self.name_2: 0}

    def game_stat_print(self):  # печатает статус игры словами из словаря
        print('{:^30}'.format(self.game_state_dict[self.game_state]))

    def change_game_state(self, game_state):  # Меняет статус игры
        self.game_state = game_state

    def move(self, player, cell):  # Ход игрока
        if isinstance(player, Player):
            self.board_value.board[cell - 1].empty = player.figure

    def cell_check(self, number):  # Проверка клетки, свободна или нет
        if self.board_value.board[number - 1].empty_status():
            return True
        else:
            return False

    # Можно ли было как-то компактенее записать условия для победы?

    def win(self):  # Условия для победы, проверка победа или нет
        for i in self.vin_list:
            if (self.board_value.board[i[0]] ==
                    self.board_value.board[i[1]] ==
                    self.board_value.board[i[2]] ==
                    ' X '):
                return True
            elif (self.board_value.board[i[0]] ==
                  self.board_value.board[i[1]] ==
                  self.board_value.board[i[2]] ==
                  ' O '):
                return True
            else:
                return False

    def start_game(self):  # Начало игры
        play_again = True
        while play_again:
            print('{:^30}'.format('Игра началась'))
            self.board_value.display()
            count = 1
            while self.game_state < 3:
                try:
                    if count % 2:
                        cell = int(input(f'{self.name_1} введите номер ячейки куда будете ходить?'))
                        if cell > 9:
                            raise ValueError
                        current_player = self.players[0]
                        if self.cell_check(cell):
                            self.move(self.players[0], cell)
                        else:
                            print('Клетка занята')
                            continue
                    else:
                        cell = int(input(f'{self.name_2} введите номер ячейки куда будете ходить?'))
                        if cell > 9:
                            raise ValueError
                        current_player = self.players[1]
                        if self.cell_check(cell):
                            self.move(self.players[1], cell)
                        else:
                            print('Клетка занята')
                            continue
                    os.system('cls')  # Вот эта штука работает лишь в консоли виндовс
                    self.board_value.display()
                    count += 1
                    if self.win():
                        self.change_game_state(3)
                        self.game_stat_print()
                        self.score[current_player.name] += 1
                        print('{:^30}'.format('Победил ' + current_player.name))
                    elif count == 9:
                        self.change_game_state(4)
                        self.game_stat_print()
                    else:
                        self.change_game_state(2)
                        self.game_stat_print()
                except ValueError:
                    print('Ввел слишком большой номер ячейки. Попробуй еще раз')
            print(f'   Счет {self.name_1} - {self.score[self.name_1]} : {self.name_2} - {self.score[self.name_2]}')
            revenge = input('Реванш будет? (1/0)')
            if revenge == '0':
                print('Пока!')
                break
            elif revenge == '1':
                self.board_value = Board()
                self.change_game_state(1)


print('Задача 06. Крестики-нолики')

game_1 = Game('Боря', 'Катя', )
game_1.start_game()
