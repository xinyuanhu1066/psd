import random


def generate_random_word():
    words = ['lion', 'leopard', 'tiger', 'jaguar', 'cheetah', 'cougar']
    index = random.randrange(len(words))
    return words[index]


def generate_blanks(word):
    indices = [random.randint(0, len(word)-1) for i in range(len(word)-1)]
    blanked_word = list(word)
    for i in indices:
        blanked_word[i] = ' '
    return (word, blanked_word)


def run_game(word_info, lives):
    left_lives = lives
    target_word, blanked_word = word_info
    while True:
        print(f'The word is {blanked_word}')
        letter = input('Please guess a letter: ')
        if letter in target_word:
            for index, current_letter in enumerate(target_word):
                if current_letter == letter and blanked_word[index] == ' ':
                    blanked_word[index] = letter
                    break
            if blanked_word.count(' ') == 0:
                print('You win!')
                break
        else:
            left_lives -= 1
            if left_lives == 0:
                print(f'You lose! The word is: {target_word}')
                break


if __name__ == '__main__':
    word = generate_random_word()
    run_game(generate_blanks(word), 5)
