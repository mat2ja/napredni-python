'''
Neka je zadan niz trojki (x, a, b) gdje je x neka aktivnost, a je vremenski početak
te aktivnosti, a b završetak. Na primjer, (’T’, (2, 13), (2, 17)) znači da aktivnost
T počinje u 2:13, a završava u 2:17. Dvije aktivnosti su kompatibilne ako se
ne preklapaju. Napišite program koji će za niz aktivnosti odabrati najveći broj
kompatibilnih aktivnosti koje se mogu smjestiti u neki zadani vremenski interval
tako da ostane što manje neispunjenog vremena tog intervala. Na primjer, za niz
aktivnosti

('F', (1, 10), (1, 20))
('G', (1, 15), (1, 19))
('A', (1, 12), (1, 14))
('R', (1, 4), (1, 55))

i vremenski interval (1:00, 1:20), optimalni izbor aktivnosti je skup {(’A’, (1, 12),
(1, 14)), (’G’, (1, 15), (1, 19))}
'''


lst = [[-4, 1], [1, 5], [2, 10], [3, 5], [1, 3], [3, 8], [8, 12], [5, 11]]
lst = [[110, 120], [115, 119], [112, 114], [14, 155]]


def longest(lst):
    mx = (0, [])
    for i in range(1, len(lst) - 1):    # test for all following and acceptable elements
        if lst[i][0] == lst[0][1]:
            add = longest(lst[i:])
            if add[0] > mx[0]:         # keep "longest" chain
                mx = add
    #print(lst, mx)
    return (lst[0][1] - lst[0][0] + mx[0], [lst[0]] + mx[1])


# chain elements must be in increasing order
# print(longest(sorted(lst)))


def toMinutes(interval):
    sati, minute = interval
    return sati * 60 + minute


def aktivnostiIntervala(aktivnosti, interval):
    akt_u_intervalu = []
    minterval = (toMinutes(interval[0]), toMinutes(interval[1]))
    for aktivnost in aktivnosti:
        _, poc, kraj = aktivnost
        mpoc = toMinutes(poc)
        mkraj = toMinutes(kraj)
        if mpoc >= minterval[0] and mkraj <= minterval[1]:
            akt_u_intervalu.append(aktivnost)
    return akt_u_intervalu


def optimal(aktivnosti, interval, rez=[]):
    aktivnosti = aktivnostiIntervala(aktivnosti, interval)
    vrijeme = toMinutes(interval[1]) - toMinutes(interval[0])

    for i in range(0, len(aktivnosti)):
        _, poc, kraj = aktivnost = aktivnosti[i]
        mpoc = toMinutes(poc)
        mkraj = toMinutes(kraj)
        novo_vrijeme = vrijeme - (mkraj - mpoc)
        preklapanje = False
        for r in rez:
            _, rezpoc, rezkraj = r
            rpoc = toMinutes(rezpoc)
            rkraj = toMinutes(rezkraj)
            if (set(range(rpoc, rkraj)).intersection(range(mpoc, mkraj))):
                preklapanje = True
                break

        if novo_vrijeme > 0 and not preklapanje:
            vrijeme = novo_vrijeme
            rez.append(aktivnost)
        else:
            break
    return rez


aktivnosti = [
    ('F', (1, 10), (1, 20)),
    ('G', (1, 15), (1, 19)),
    ('A', (1, 12), (1, 14)),
    ('R', (1, 4), (1, 55))
]

# aktivnosti = [
#     ('F', (110), (120)),
#     ('G', (115), (119)),
#     ('A', (112), (114)),
#     ('R', (14), (155))
# ]

print(optimal(aktivnosti, ((1, 0), (1, 20))))
