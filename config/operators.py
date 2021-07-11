# Dict of SQL operators
operators_dict = {}

# SQL arithmetic operators
key = 'ADD_OP'
operators_dict[key] = {'repr': '+'}
help_str = ''

key = 'SUBTRACT_OP'
operators_dict[key] = {'repr': '-'}

key = 'MULTIPLY_OP'
operators_dict[key] = {'repr': '*'}

key = 'DIVIDE_OP'
operators_dict[key] = {'repr': '/'}

key = 'MODULO_OP'
operators_dict[key] = {'repr': '%'}

# SQL bitwise operators
key = 'BITWISE_AND_OP'
operators_dict[key] = {'repr': '&'}

key = 'BITWISE_OR_OP'
operators_dict[key] = {'repr': '|'}

key = 'BITWISE_EXCLUSIVE_OR_OP'
operators_dict[key] = {'repr': '^'}

# SQL comparison operators
key = 'EQUAL_TO_OP'
operators_dict[key] = {'repr': '='}

key = 'GREATER_THAN_OP'
operators_dict[key] = {'repr': '>'}

key = 'LESS_THAN_OP'
operators_dict[key] = {'repr': '<'}

key = 'GREATER_THAN_EQUAL_TO_OP'
operators_dict[key] = {'repr': '>='}

key = 'LESS_THAN_EQUAL_TO_OP'
operators_dict[key] = {'repr': '<='}

key = 'NOT_EQUAL_TO_OP'
operators_dict[key] = {'repr': '<>'}
