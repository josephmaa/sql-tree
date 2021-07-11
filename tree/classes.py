import csv
import re

from config import params_config
from Typing import List
from utils import isValidIdentifier


class ParseTree():
    def __init__():
        pass


class SQLQuery():
    """
    Create a SQLQuery class that is the main wrapper for the parser. Query results are also themselves trees. The tree will be of the format: 

    SQLQuery -|- SELECT
              |- COLUMNS
              |- FROM
              |- TABLES (SQLQuery objects)

    Terminals are leaf nodes of the final parse query tree. (i.e identifiers like column names and provided tables)

    Input:
        tokens                              List[str]

    Output:
        nodes                               List[tuple]
        edges                               List[tuple]

    """

    def __init__(self, tokens: List[str]):
        self.state = 'WAITING'
        self.statement = ''
        self.nodes = []
        self.edges = []
        try:
            # main logic loop
            for token in tokens:
                if self.statement == '':
                    # if self.statement has no statements, then the loop must have just started
                    # or there must be multiple fields that are getting input to the node
                    if token in params_config:
                        # do need to update the state
                        self.state = params_config[token]
                        self.statement = token
                    elif isValidIdentifier(token):
                        # do need to update the statement
                        self.statement = token
                    else:
                        raise SyntaxError
                else:
                    # self.statement must contain some field, so update the nodes. Consider
                    # whether we need to also update the state
                    if token in params_config:
                        # do need to update the previous statement
                        self.nodes.
                        # do need to update the state
                        self.state = params_config[token]
                        self.statement = token
                    elif token == ',':
                        self.statement = ''
                    elif isValidIdentifier(token):
                        self.n

                elif token == ',':
                    # don't need to update the state
                    # do need to update the node list
                    self.nodes.append(self.statement)

                # termination condition for query
                if token == ';':

                    self.state = 'COMPLETED'
        except SyntaxError:
            print('SyntaxError in SQL Query')

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges


class Lexer():
    """
    Lexer tokenizes query into lexemes and categorizes them by token category.
    """

    def __init__(self, pathToRawInput: str):
        self.pathToRawInput = pathToRawInput

    def tokenizeInput(self):
        """
        Tokenize csv file from raw input into list of queries.

        Input:
            self.path_to_raw_input          str
        Output:
            queries                         List[str]
        """
        with open(self.pathToRawInput, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            # The header of the reader are columns, so skip the first column
            next(reader)
            queries = []
            for row in reader:
                queries.extend([query.strip()
                                for query in row if query != ''])
            return queries

    def tokenizeQuery(self, query: str):
        """
        Contains the main logic for parsing queries from tokenizeInput into 
        lexemes for use by the semantic analyzer.

        Input:
            query                           str
        Output:
            tokenizedQuery                  list[str]
        """
        tokenizedQuery = []
        for segment in query.split(' '):
            regex = re.split('(,)', segment)
            filteredRegex = filter(lambda s: not(s == ''), regex)
            tokenizedQuery.extend(filteredRegex)
        tokenizedQuery.append(';')
        return tokenizedQuery
