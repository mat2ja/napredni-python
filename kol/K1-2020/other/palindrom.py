f = open(r'files/palindromi.txt', 'r')
redovi = [red[:-1] for red in f]


def is_palindrom(str):
    return len(str) > 1 and str == str[::-1]


def count_palindroms(redovi):
    count = 0
    for red in redovi:
        if is_palindrom(red):
            count += 1
    return count


print(count_palindroms(redovi))
