import re
'''
a) Napišite program koji će upotrebom regularnih izraza pronaći u tekstu sve
brojeve telefona napisane u obliku XXX-XXXX-XXX, gdje je X neka zna-
menka.
'''
r_a = r'[\d]{3}-[\d]{4}-[\d]{3}'
a1 = '123-2344-123'
a2 = '121-2323-121-3232-322-3223-332'
rez_a1 = re.match(r_a, a1)
rez_a2 = re.match(r_a, a2)

print('\na)')
print(rez_a1)
print(rez_a2)

'''
(b) Riješite prethodni zadatak tako da prve tri znamenke broja telefona mogu
biti opcionalne.
'''
r_b = r'([\d]{3}-)?[\d]{4}-[\d]{3}'
b1 = '123-2344-123'
b2 = '2344-123'
b3 = '-2344-123'
rez_b1 = re.match(r_b, b1)
rez_b2 = re.match(r_b, b2)
rez_b3 = re.match(r_b, b3)

print('\nb)')
print(rez_b1)
print(rez_b2)
print(rez_b3)


'''
(c) Napišite program koji će upotrebom regularnih izraza u tekstu zamijeniti sve
datume oblika DD.MM.GGGG. nizom slova X.
'''
r_c = r'[\d]{1,2}\.[\d]{1,2}\.[\d]{4}\.'
test_str = '12.12.1999. 10.2.2332. 2.222.1933. 1.1.1999. 2.2.2222 .1.8.2002.'
c_matches = re.findall(r_c, test_str)
rez_c = test_str
for match in c_matches:
    rez_c = rez_c.replace(match, 'XX.XX.XXXX.')
print('\nc)')
print('')
print(rez_c)


'''
Napišite program koji će upotrebom regularnih izraza u tekstu naći sve dijelove koji se nalaze u uglatim zagradama i ispisati samo te dijelove.
'''
r_d = r'(?<=\[)[^][]*(?=])'
zen = 'Beautiful is [better] than (ugly). [Explicit is better than [implicit]. [Simple] is better than complex.'
rez_d = re.findall(r_d, zen)
print('\nd)')
print(rez_d)


'''
2. Za zadatke 1a i 1b nacrtajte konačne automate (deterministične ili nedeterminis-
tične).
'''

'''
3. Za regularni izraz (a*|b)(ab)* nacrtajte konačni automat i napišite tablicu prelaza.
'''
prijelazi_z3 = {
    0: {'a': {0}, 'ø': {1}},
    1: {'b': {2}},
    2: {'a': {1}}
}

'''
4. Definirajte regularni izraz za heksadecimalne brojeve.
'''
r4 = r'(0[xX])?[\da-fA-F]+'
test_4_1 = '0x0f4'
test_4_2 = '0acdadecf822eeff32aca5830e438cb54aa722e3'
test_4_3 = '8BADF00D'
rez_4_1 = re.fullmatch(r4, test_4_1)
rez_4_2 = re.fullmatch(r4, test_4_2)
rez_4_3 = re.fullmatch(r4, test_4_3)
print('\n4)')
print(rez_4_1)
print(rez_4_2)
print(rez_4_3)


'''
5. Definirajte regularni izraz za rimske brojeve.
'''
r_5 = r'^M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$'
test_5 = 'MMMCMXCIX'
rez_5 = re.match(r_5, test_5)
print('\n5)')
print(rez_5.group(0))

'''
6. Za konačni automat na slici 1.7 napišite odgovarajući regularni izraz.
'''
r_6 = r'(a?a+bb{1,})*'
test_6_1 = 'aaabb'
test_6_2 = 'abb'

'''
7. Nacrtajte konačni automat (deterministični ili nedeterministični) i napišite odgo-
varajući regularni izraz za nizove znamenki gdje se niti jedna znamenka ne ponavlja.
'''
prijelazi_z7 = {}
r_7 = r''


'''
8. Implementirajte konačni automat sa slike 1.4 pomoću tablice prelaza.
'''
prijelazi_z8 = {
    0: {'a': {0}, 'b': {0}},
    1: {'a': {1}, 'b': {1}},
    2: {'a': {2}, 'b': {2}, 'e': {0}},
    3: {},
}
