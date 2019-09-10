import os

def clear():
    """Clears console lines."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')