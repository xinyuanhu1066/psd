'''Implementation of arithmetic functions'''

import unittest


def add(x, y):
    '''Function for +'''
    return x + y


def multiply(x, y):
    '''Function for *'''
    return x * y


def substract(x, y):
    '''Function for -'''
    return x - y


def divide(x, y):
    '''Function for /'''
    if y == 0:
        return None
    return x / y


def modular(x, y):
    '''Function for %'''
    if y == 0:
        return None
    return x % y


class TestMathOperation(unittest.TestCase):
    '''Unit test class'''

    def test_add(self):
        '''Test method of add function'''
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        '''Test method of multiply function'''
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_substract(self):
        '''Test method of substract function'''
        self.assertEqual(substract(2, 1), 1)
        self.assertEqual(substract(1, 1), 0)
        self.assertEqual(substract(1, 3), -2)

    def test_divide(self):
        '''Test method of divide function'''
        self.assertEqual(divide(3, 1), 3)
        self.assertIsNone(divide(1, 0))
        self.assertEqual(divide(0, 2), 0)

    def test_modular(self):
        '''Test method of modular function'''
        self.assertEqual(modular(1, 2), 1)
        self.assertEqual(modular(3, 1), 0)
        self.assertIsNone(modular(1, 0))


if __name__ == '__main__':
    unittest.main()
