import random

def onedie():
    return random.randrange(1, 6, 1)
def twodie():
    return onedie() + onedie()
