class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)

    def length(self):
        return len(self.text)

    def upper(self):
        return self.text.upper()


if __name__ == '__main__':
    name = StringManipulator('example')
    result = name.find_character('x')
    print(f'\nThe index is {result}\n')
    print(f'The length of is: {name.length()}')
    print(f'\nThe uppercase is: {name.upper()}\n')
