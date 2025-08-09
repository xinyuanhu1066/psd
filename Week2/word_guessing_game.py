import random
import re


def generate_random_word():
    """Return a random word from a pre-defined word list."""
    words = ['lion', 'leopard', 'tiger', 'jaguar', 'cheetah', 'cougar']
    return random.choice(words)


def initialise_blanks(word):
    """Create several blanks according to the length of word."""
    return ['_' for _ in word]


def fill_blanks(blanks, orig_word, letter):
    """Replace blanks correspond to all the occurrences of the
       letter in the original word.
    """
    for index, char in enumerate(orig_word):
        if char == letter:
            blanks[index] = letter


def display_blanks(blanks):
    """Print the current blank list, each item is separated by a space."""
    print(' '.join(blanks))


def run_game(lives=5):
    """Main game loop."""
    word = generate_random_word()
    blanks = initialise_blanks(word)
    left_lives = lives
    tried_letters = set()

    print('\nWelcome to Word Guessing!')
    print(f'The word has {len(word)} letters, and you have {left_lives} lives.')

    while True:
        display_blanks(blanks)
        user_guess = input('Please guess a letter: ').lower()
        # Check user input is only a single letter
        if not re.match(r'^[a-z]$', user_guess):
            print('Invalid input, please type a single letter.')
            continue
        # Check if user has already used the letter
        if user_guess not in tried_letters:
            tried_letters.add(user_guess)
        else:
            print(f'You have tried this letter. Your lives is {left_lives}.\n')
            continue
        if user_guess in word:
            fill_blanks(blanks, word, user_guess)
            #Check if all blank fields are filled
            if blanks.count('_') == 0:
                print('\nCongratulations!')
                print(f'The word is: {word}\n')
                break
            else:
                print('Good job!\n')
        else:
            left_lives -= 1
            print(f'Wrong letter, you have {left_lives} lives left.\n')
            if left_lives == 0:
                print(f'\nGame over!')
                print(f'The word is: {word}\n')
                break


if __name__ == '__main__':
    run_game()
