# Dict of SQL class
params_dict = {}

key = 'SELECT'
params_dict[key] = 'PROJECT'

key = 'SUM'
params_dict[key] = 'PROJECT'

key = 'FROM'
params_dict[key] = 'JOIN'

key = 'JOIN'
params_dict[key] = 'JOIN'

key = 'WHERE'
params_dict[key] = 'RESTRICT'


# TODO(joseph): not too sure about implementing this functionality, since TABLE doesn't seem like it'll be used frequently 
# key = 'SORT'
# params_dict[key] = set([])

# key = 'TABLE'
# params_dict[key] = set([])
