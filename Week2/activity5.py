class SentenceInspector:
    def __init__(self, sentence):
        self.sentence = sentence

    def get_words_num(self):
        """Return the number of words in the sentence."""
        # split the string by space and count the length of the array
        return len(self.sentence.split(' '))
    

def main():
    sentence = input('Please input a sentence: ')
    inspector = SentenceInspector(sentence)
    print(f'The number of words:', inspector.get_words_num())


if __name__ == '__main__':
    main()