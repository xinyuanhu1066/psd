'''Tic Tac Toe game implementation'''

import re
import random
import select
import sys
from prettytable import PrettyTable, HRuleStyle, VRuleStyle


COLUMN_LETTERS = ['A', 'B', 'C']
TIMEOUT = 10


class Board:
    '''Game board'''
    def __init__(self):
        self.__matrix = [
            [''] * 3,
            [''] * 3,
            [''] * 3,
        ]

    def display(self):
        '''Print current board marks in console'''
        print()
        table = PrettyTable()
        table.hrules = True
        table.vrules = True
        table.padding_width = 1
        table.preserve_internal_border = True
        table.field_names = [' '] + COLUMN_LETTERS
        table.add_rows([[index + 1] + row for index, row in enumerate(self.__matrix)])
        table_str = str(table).splitlines()
        table_str = table_str[1:]
        lines = [line[1:] for line in table_str]
        print('\n'.join(lines))
        print()

    def place_mark(self, mark, coordinate):
        '''Set a mark into board with its coordinate'''
        column_letter, row_index = re.match(r'([a-cA-C])(\d)', coordinate).groups()
        column_index = ord(column_letter.lower()) - ord('a')
        row_index = int(row_index) - 1
        if self.__matrix[row_index][column_index] != '':
            return False
        self.__matrix[row_index][column_index] = mark
        return True

    def is_mark_in_straight_line(self, mark):
        '''Check if there are three marks in one line'''
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
    '''Game player'''
    def __init__(self, name, auto_place=False):
        self.__name = name
        self.__auto_place = auto_place
        self.__mark = ''

    @property
    def name(self):
        '''Return player'name'''
        return self.__name

    @property
    def auto_place(self):
        '''Return if the player places mark automatically'''
        return self.__auto_place

    @property
    def mark(self):
        '''Return the mark's value'''
        return self.__mark

    @mark.setter
    def mark(self, value):
        self.__mark = value

    def move(self, game_board):
        '''Prompt the user to input coordinate or use random
           coordinate if auto_place=True, and then update game
           board.'''
        time_left = TIMEOUT
        while True:
            if self.__auto_place:
                coordinate = COLUMN_LETTERS[random.randint(0,2)] + str(random.randint(1,3))
                print(f'{self.__name} moves to: {coordinate}')
            else:
                while time_left > 0:
                    time_left -= 1
                    self._prompt(f'{self.__name} moves to ({time_left} seconds left): ')
                    read_list, _, _ = select.select([sys.stdin], [], [], 1.0)
                    if len(read_list) > 0:
                        coordinate = sys.stdin.readline().strip()
                        if re.match(r'[a-cA-C]\d', coordinate):
                            break
                        print('\nInvalid coordinate! Example: A1, B2\n')
                if time_left == 0:
                    print('\nYour turn is timeout!\n')
                    return False
            if game_board.place_mark(self.__mark, coordinate):
                return True
            print('\nThis place is taken. Try another one.\n')

    def _prompt(self, message):
        # save cursor position
        sys.stdout.write('\x1b[s')
        # move cursor to upper line and clear it
        sys.stdout.write('\x1b[1A\x1b[2K')
        sys.stdout.write(f'{message}\n')
        # restore cursor position
        sys.stdout.write('\x1b[u')
        sys.stdout.flush()


class Game:
    '''Game controller'''
    def __init__(self, game_board, game_players):
        self.__board = game_board
        self.__players = game_players
        self.__turn_index = 0
        self.__winner = None

    def run(self):
        '''Main game logic'''
        print('\nWelcome to Tic Tac Toe game!\n')
        self._get_x_or_o()
        self.__board.display()
        while True:
            player = self._next_player()
            if not player.move(self.__board):
                continue
            self.__board.display()
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
        game_players = {}
        for player in self.__players:
            game_players[player.mark] = player
        for mark in ['x', 'o']:
            if self.__board.is_mark_in_straight_line(mark):
                self.__winner = game_players[mark]
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
