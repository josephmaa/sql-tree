import unittest

from tree.classes import Lexer, Node, SQLQuery
from tree.utils import isValidIdentifier


class testParser(unittest.TestCase):
    """
    Tests assume that input to the parser are valid.
    """

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
        identifiers = ['test', '0test', 'test_', 'test__', 'TEST']
        areValidIdentifiers = [True, False, False, False, True]
        self.assertEqual([isValidIdentifier(id)
                          for id in identifiers], areValidIdentifiers)

    def testNode(self):
        label, attribute, value = 'SELECT_TEST', 'SELECT', None
        # Just check if the node is create correctly
        Node(label=label, attributes={attribute: value})

    def testSQLQuery(self):
        """
        Test main logic of SQLQuery class:
        """
        tokens = ['SELECT', 'id', ',', 'people', 'FROM', 'users', ';']
        self.assertEqual([str(n) for n in SQLQuery(tokens=tokens).nodes], [
                         '(SELECT,{})', "(SELECT_LIST,{'id': None, 'people': None})", '(FROM,{})', "(FROM_LIST,{'users': None})"])


if __name__ == '__main__':
    unittest.main()
