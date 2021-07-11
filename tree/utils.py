
def isValidIdentifier(token: str):
    """
    Checks whether token is a valid identifier according to SQL grammar
    """
    return bool(re.search('^[a-zA-Z](?:_?[a-zA-Z0-9]+)*$', token))
