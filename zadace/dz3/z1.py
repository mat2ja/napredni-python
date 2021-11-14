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
