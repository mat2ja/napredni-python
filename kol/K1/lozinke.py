'''
kolko ima lozinki u fileu a lozinka mora sadrzavat velika i mala slova, brojeve i posebne znakove s tim da broj slova>broj brojeva>broj posebnih znakova
'''


f = open(r'files/lozinke.txt', 'r')
redovi = [red[:-1] for red in f]


def count_numbers(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count


def count_letters(string):
    count = 0
    for i in string:
        if i.isalpha():
            count += 1
    return count


def count_special_characters(string):
    count = 0
    for i in string:
        if not i.isalpha() and not i.isdigit():
            count += 1
    return count


def count_capitalized_letters(string):
    count = 0
    for i in string:
        if i.isupper():
            count += 1
    return count


def count_lower_case_letters(string):
    count = 0
    for i in string:
        if i.islower():
            count += 1
    return count


def contains_all(password):
    return count_capitalized_letters(password) > 0 and count_lower_case_letters(password) > 0 and count_numbers(password) > 0 and count_special_characters(password) > 0


def follows_rules(password):
    return count_letters(password) > count_numbers(password) and count_numbers(password) > count_special_characters(password)


def count_passwords(lista):
    count = 0
    for password in lista:
        if contains_all(password) and follows_rules(password):
            count += 1
    return count


print(count_passwords(redovi))
