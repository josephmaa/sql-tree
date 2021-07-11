import unittest

from tree.classes import Lexer


class testLexer(unittest.TestCase):
    def testTokenizeInput(self):
        """
        Test tokenize input functionality
        """
        input = 'tests/queries.txt'
        lexer = Lexer(pathToRawInput=input)
        self.assertEqual(
            lexer.tokenizeInput(),
            ['SELECT id, people FROM users', 'SELECT tomato FROM fruits',
             'SELECT Name, OrderDate FROM Customer, Order WHERE Order."OrderDate" = Order."ShipDate"']
        )

    def testTokenizeQuery(self):
        """
        Test tokenize query functionality
        """
        input = 'SELECT id, people FROM users'
        lexer = Lexer(pathToRawInput='')
        self.assertEqual(
            lexer.tokenizeQuery(input),
            ['SELECT', 'id', ',', 'people', 'FROM', 'users']
        )

    def testTokenizeQueryComplex(self):
        """
        Test tokenize query functionality on more complex query
        """
        input = 'SELECT Name, OrderDate FROM Customer, Order WHERE Order."OrderDate" = Order."ShipDate"'
        lexer = Lexer(pathToRawInput='')
        self.assertEqual(lexer.tokenizeQuery(input),
                         ['SELECT', 'Name', ',', 'OrderDate', 'FROM', 'Customer', ',',
                             'Order', 'WHERE', 'Order."OrderDate"', '=', 'Order."ShipDate"']
                         )


if __name__ == '__main__':
    unittest.main()
