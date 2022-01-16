'''
5 ih je vecih od 10 znakova nakon sto se znak ne ponavljuje?
'''

f = open(r'files/palindromi.txt', 'r')
redovi = [red[:-1] for red in f]


def is_palindrom(str):
    return str == str[::-1]


def is_valid(str):
    long_enough = len(str) > 10
    return long_enough


def count_palindroms(redovi):
    count = 0
    for red in redovi:
        if is_palindrom(red) and is_valid(red):
            count += 1
    return count


print(count_palindroms(redovi))
