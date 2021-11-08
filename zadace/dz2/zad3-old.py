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


def leftoverTime(timeline, interval):
    vrijeme = toMinutes(interval[1]) - toMinutes(interval[0])
    for _, poc, kraj in timeline:
        vrijeme -= (toMinutes(kraj) - toMinutes(poc))
    return vrijeme


def by_duration(aktivnost):
    _, poc, kraj = aktivnost
    trajanje = toMinutes(kraj) - toMinutes(poc)
    return trajanje


def optimal(aktivnosti, interval, final=[]):
    aktivnosti = aktivnostiIntervala(aktivnosti, interval)
    aktivnosti.sort(key=by_duration, reverse=True)

    rezultati = []
    for i in range(0, len(aktivnosti)):
        rez = []
        vrijeme = toMinutes(interval[1]) - toMinutes(interval[0])
        while vrijeme > 0:
            for j in range(i, len(aktivnosti)):
                preklapanje = False
                _, poc, kraj = aktivnost = aktivnosti[j]
                npoc = toMinutes(poc)
                nkraj = toMinutes(kraj)
                vrijeme = toMinutes(interval[1]) - toMinutes(interval[0])
                for r in rez:
                    rpoc = toMinutes(r[1])
                    rkraj = toMinutes(r[2])
                    if (set(range(rpoc, rkraj)).intersection(range(npoc, nkraj))):
                        preklapanje = True
                        break

                if not preklapanje:
                    vrijeme -= (nkraj - npoc)
                    rez.append(aktivnost)

            break

        rezultati.append(rez)

        vise_aktivnosti = len(rez) > len(final)
        if not final or vise_aktivnosti:
            final = rez

    return final


aktivnosti = [
    ('F', (1, 10), (1, 20)),
    ('G', (1, 15), (1, 19)),
    ('A', (1, 12), (1, 14)),
    ('R', (1, 4), (1, 55))
]

print(optimal(aktivnosti, ((1, 0), (1, 20))))
