class StringManipulator:
    def find_character(self, text, char):
        return text.find(char)

    def length(self, text):
        return len(text)

    def upper(self, text):
        return text.upper()


def main():
    test_str = 'example'
    test_char = 'x'
    name = StringManipulator()
    index = name.find_character(test_str, test_char)
    print(f'\nThe text is: "{test_str}"')
    print(f'\nThe index of "{test_char}" is: {index}\n')
    print(f'The length of "{test_str}" is: {name.length(test_str)}')
    print(f'\nThe uppercase of "{test_str}" is: {name.upper(test_str)}\n')


if __name__ == '__main__':
    main()
