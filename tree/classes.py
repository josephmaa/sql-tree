import csv
import re


class Parser():
    def __init__():
        pass


class Query():
    def __init__():
        pass


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
            queries                         list
        """
        with open(self.pathToRawInput, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            # The header of the reader are columns, so skip the first column
            next(reader)
            queries = []
            for row in reader:
                queries.extend([query.strip() for query in row if query != ''])
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
        return tokenizedQuery
