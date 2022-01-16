import re


'''
Za sljedeću tablicu prijelaza definirajte regularni izraz i pomoću njega napišite
program u Pythonu koji će dati odgovor na sljedeće pitanje: Koliko redova u datoteci
"fsa-2.txt" odgovara tom regularnom izrazu?
Stanja su u prvom stupcu, a ulazni simboli u prvom redku. Stanje označeno s "!" je
konačno stanje.
'''

'''
----------------- 1.
    x  y  .
0!  2 
1      1  3 
2   2  1
3         0

'''


'''
----------------- 1.
(x+y+.{2})*
'''

# search je za trazenje uzorka bilgodje u zadanom stringu
# a match odustane cim ne nade uzroak na pocetku, cak i da uzorak bude negdje u sredini, vratit ce None


def count_matches(regex, strings):
    count = 0
    for string in strings:
        # TODO match vs search
        found = re.search(regex, string)
        if found:
            print('MATCHED', found)
            count += 1
    return count


r1 = r'(x+y+\.{2})+'
redovi = [
    'xxyy..',
    'xxyyf.',
    'xxyy...xxy.',
    'xy..',
]
# print('1)', count_matches(r1, redovi))


'''
----------------- 2.
    €  p  m  t  .  ,
0!  1  1
1         2  2 
2               3  1
3!         

'''


'''
----------------- 2.
p?(m|t)(\.|,)
'''

r2 = r'p?(m|t)(\.|,)'
# r2 = 'p?[mt][\.,]'
redovi2 = [
    'pm.',
    'pm.',
    't.,',
    'm.',
    'm,',
    'patrik'
    'patrik t,'  # ne prepozna s match ali da sa search
]
# print('2)', count_matches(r2, redovi2))


'''
----------------- 3.
    a  b  c  d  Ɛ
0!  1
1      3
2            0  0
3         2
'''

'''
----------------- 3.
(abcd?)+
'''


r3 = r'(abcd?)+'
redovi3 = [
    'abcd',
    'abcabcd',
    'abcabcfdfd',
    'fdsfdabcd'
]
print('3)', count_matches(r3, redovi3))
