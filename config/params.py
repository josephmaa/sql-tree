# Dict of SQL class
params_dict = {}

key = 'restrict'
params_dict[key] = set(['WHERE', 'JOIN'])
help_str = ''

key = 'project'
params_dict[key] = set(['SELECT', 'SUM']),

key = 'join'
params_dict[key] = set(['FROM', 'JOIN'])

key = 'sort'
params_dict[key] = set([])

key = 'table'
params_dict[key] = set([])
