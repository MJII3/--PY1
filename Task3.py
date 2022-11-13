import random

symbol = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def get_random_password( a, n=8):
    for x in range(a):
        password = ''
        for x in range(n):
            password += random.choice(symbol)
        return password



print(get_random_password(1))
