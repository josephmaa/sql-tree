import unittest

from tree.classes import Lexer, SQLQuery


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
            ['SELECT', 'id', ',', 'people', 'FROM', 'users', ';']
        )

    def testTokenizeQueryComplex(self):
        """
        Test tokenize query functionality on more complex query
        """
        input = 'SELECT Name, OrderDate FROM Customer, Order WHERE Order."OrderDate" = Order."ShipDate"'
        lexer = Lexer(pathToRawInput='')
        self.assertEqual(lexer.tokenizeQuery(input),
                         ['SELECT', 'Name', ',', 'OrderDate', 'FROM', 'Customer', ',',
                             'Order', 'WHERE', 'Order."OrderDate"', '=', 'Order."ShipDate"', ';']
                         )
    
    def testIsValidIdentifierRegex(self):
        """
        Test regex search for some known valid identifiers and invalid identifiers
        """
        queries = SQLQuery(tokens=[])
        identifiers = ['test', '0test', 'test_', 'test__', 'TEST']
        areValidIdentifiers = [True, False, True, False, True]
        self.assertEqual()
    


if __name__ == '__main__':
    unittest.main()
