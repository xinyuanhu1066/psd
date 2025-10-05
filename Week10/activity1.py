'''Module providing a class parsing string.'''

import re


class StringOperator:
    '''Contains methods of parsing strings.'''
    def __init__(self, source):
        self.source = source

    def total_length(self):
        '''Calculates the total length.'''
        return len(self.source)

    def upper_letters_num(self):
        '''Determines the number of uppercase characters.'''
        num = 0
        for item in self.source:
            result = re.findall(r'[A-Z]', item)
            num += len(result)
        return num


if __name__ == '__main__':
    TEST_STRING = 'test Test Hello World'
    operator = StringOperator(TEST_STRING)
    print('Test string:', TEST_STRING)
    print('Total length:', operator.total_length())
    print('Number of uppercase letters:', operator.upper_letters_num())
