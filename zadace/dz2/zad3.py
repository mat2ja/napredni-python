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


def toMinutes(interval):
    sati, minute = interval
    return sati * 60 + minute


def rangeMap(niz):
    range_map = {}
    for akt, poc, kraj in niz:
        range_map[akt] = range(toMinutes(poc), toMinutes(kraj))
    return range_map


def optimal(niz):
    range_map = rangeMap(niz)
    print(range_map)

    termini = []
    range_list = list(range_map.items())
    for i in range(0, len(range_list)):
        akt = range_list[i]
        optimalno = [niz[i]]
        for j in range(i+1, len(range_list)):
            slj_akt = range_list[j]
            has_interesection = set(akt[1]).intersection(slj_akt[1])
            if not has_interesection:
                has_internal_intersection = False
                for k in range(1, len(optimalno)):
                    akt_ime = optimalno[k][0]
                    if (akt_ime == slj_akt[0]):
                        continue
                    nova_akt = (akt_ime, range_map[akt_ime])
                    has_interesection = set(
                        slj_akt[1]).intersection(nova_akt[1])
                    if has_interesection:
                        has_internal_intersection = True
                        break

                if not has_internal_intersection:
                    optimalno.append(niz[j])
        termini.append(optimalno)

    max_termin = []
    for termin in termini:
        duljina = len(termin)
        if duljina >= len((max_termin)):
            max_termin = termin

    return max_termin


aktivnosti = [
    ('F', (1, 10), (1, 20)),
    ('G', (1, 15), (1, 19)),
    ('A', (1, 12), (1, 14)),
    ('R', (1, 4), (1, 55))
]

# print(optimal(aktivnosti))


aktivnosti2 = [
    ('F', (1, 10), (1, 20)),
    ('G', (1, 15), (1, 19)),
    ('A', (1, 12), (1, 14)),
    ('R', (1, 4), (1, 55)),
    ('H', (2, 4), (2, 56)),
    ('Z', (2, 20), (2, 24)),
]

print(optimal(aktivnosti2))
