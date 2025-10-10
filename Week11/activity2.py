'''Implementation for tracking personal expenses.'''
import unittest


class ExpenseTracker:
    '''Expense tracker class'''
    def __init__(self):
        self.__expenses = []

    def add_expense(self, description, amount):
        '''Add expense function.
           Return True if adding successfuly, otherwise False.
        '''
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            return False
        if amount < 0:
            return False
        self.__expenses.append((description, amount))
        return True

    @property
    def total_expense(self):
        '''Get total amount of the recorded expenses'''
        total = 0
        for record in self.__expenses:
            total += record[1]
        print(f'Total: ${total}')
        return total


class TestExpenseTracker(unittest.TestCase):
    '''Unit tests for ExpenseTracker'''

    def test_add_expense(self):
        '''Test for ExpenseTracker.add_expense()'''
        tracker = ExpenseTracker()
        self.assertTrue(tracker.add_expense('Bread', 1.98))
        self.assertTrue(tracker.add_expense('Chicken', '8.5'))
        self.assertFalse(tracker.add_expense('Apple', 'apple'))
        self.assertFalse(tracker.add_expense('Beef', -25))

    def test_total_expense(self):
        '''Test for ExpenseTracker.total_expense'''
        tracker = ExpenseTracker()
        tracker.add_expense('Bread', 1.98)
        tracker.add_expense('Chicken', '8.5')
        tracker.add_expense('Apple', 6.8)
        self.assertEqual(tracker.total_expense, 17.28)


if __name__ == '__main__':
    unittest.main()
