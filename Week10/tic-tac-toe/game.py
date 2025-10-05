import re
import random


COLUMN_LETTERS = ['A', 'B', 'C']


class Board:
    def __init__(self):
        self.__matrix = [
            [''] * 3,
            [''] * 3,
            [''] * 3,
        ]

    def display(self):
        print()
        print(' {}'.format(' '.join(COLUMN_LETTERS)))
        print()
        for index, row in enumerate(self.__matrix):
            print('{} {}'.format(index + 1, ' '.join(row)))
        print()

    def place_mark(self, mark, coordinate):
        column_letter, row_index = re.match(r'([a-cA-C])(\d)', coordinate).groups()
        column_index = ord(column_letter.lower()) - ord('a')
        row_index = int(row_index) - 1
        if self.__matrix[row_index][column_index] != '':
            return False
        self.__matrix[row_index][column_index] = mark
        return True

    def is_mark_in_straight_line(self, mark):
        for row in self.__matrix:
            if mark * 3 == ''.join(row):
                return True
        for colum in zip(*self.__matrix):
            if mark * 3 == ''.join(colum):
                return True
        lines = []
        lines.append(''.join([self.__matrix[index][index] for index in range(0, 3)]))
        lines.append(''.join([self.__matrix[index][2 - index] for index in range(0, 3)]))
        if mark * 3 in lines:
            return True
        return False


class Player:
    def __init__(self, name, auto_place=False):
        self.__name = name
        self.__auto_place = auto_place
        self.__mark = ''

    @property
    def name(self):
        return self.__name

    @property
    def auto_place(self):
        return self.__auto_place

    @property
    def mark(self):
        return self.__mark
    
    @mark.setter
    def mark(self, value):
        self.__mark = value

    def move(self, board):
        while True:
            if self.__auto_place:
                coordinate = COLUMN_LETTERS[random.randint(0,2)] + str(random.randint(1,3))
                print(f'{self.__name} moves to: {coordinate}')
            else:
                while True:
                    coordinate = input(f'{self.__name} moves to: ').strip()
                    if re.match(r'[a-cA-C]\d', coordinate):
                        break
                    print('Invalid coordinate! Example: A1, B2')
            if board.place_mark(self.__mark, coordinate):
                break
            print('This place is taken. Try another one.')


class Game:
    def __init__(self, board, players):
        self.__board = board
        self.__players = players
        self.__turn_index = 0
        self.__winner = None

    def run(self):
        self._get_x_or_o()
        while True:
            self.__board.display()
            player = self._next_player()
            player.move(self.__board)
            if self._is_game_over():
                self._print_result()
                break

    def _get_x_or_o(self):
        available_marks = ['x', 'o']
        for player in self.__players:
            if not player.auto_place:
                while True:
                    mark = input('Select a mark (x | o): ').strip().lower()
                    if mark not in ['x', 'o']:
                        print('Invalid input. Try again.')
                    elif mark not in available_marks:
                        print(f'{mark} is already selected by other player.')
                    else:
                        break
                player.mark = mark
                available_marks.remove(mark)
            else:
                player.mark = available_marks.pop()

    def _next_player(self):
        player = self.__players[self.__turn_index]
        self.__turn_index = (self.__turn_index + 1) % 2
        return player

    def _is_game_over(self):
        players = {}
        for player in self.__players:
            players[player.mark] = player
        for mark in ['x', 'o']:
            if self.__board.is_mark_in_straight_line(mark):
                self.__winner = players[mark]
                break
        if self.__winner:
            return True
        return False

    def _print_result(self):
        print()
        print('Game over!')
        print(f'Winner is {self.__winner.name}!')
        print()


if __name__ == '__main__':
    board = Board()
    players = [Player('Human'), Player('Computer', auto_place=True)]
    Game(board, players).run()
