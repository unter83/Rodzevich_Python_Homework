
def CheckSymbol(symbol):
    if str(symbol).isdigit() or (symbol == ' ' or symbol == '+'\
        or symbol == '-' or symbol == '*' or symbol == '/'\
        or symbol == '.' or symbol == ','):
        return True
    else:
        return False