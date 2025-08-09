class StringManipulator:
    # def __init__(self, text):
    #     self.text = text

    def find_character(self, char):
        return self.text.find(char)

    def length(self):
        return len(self.text)

    def upper(self):
        return self.text.upper()


def main():
    test_str = 'example'
    test_char = 'x'
    # name = StringManipulator(test_str)
    name = StringManipulator()
    # assign the "text" attribute to the object dynamically
    name.text = test_str
    index = name.find_character(test_char)
    print(f'\nThe text is: "{test_str}"')
    print(f'\nThe index of "{test_char}" is: {index}\n')
    print(f'The length of "{test_str}" is: {name.length()}')
    print(f'\nThe uppercase of "{test_str}" is: {name.upper()}\n')


if __name__ == '__main__':
    main()
