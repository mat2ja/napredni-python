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
import itertools


def toMinutes(interval):
    sati, minute = interval
    return sati * 60 + minute


def convertToRange(interval):
    _, sati, minute = interval
    return range(toMinutes(sati), toMinutes(minute))


def has_no_intersections(kombinacija):
    kombo_len = len(kombinacija)
    for i in range(0, kombo_len):
        kombo = kombinacija[i]
        nrange = convertToRange(kombo)
        for j in range(i+1, kombo_len):
            mrange = convertToRange(kombinacija[j])
            if (set(nrange).intersection(mrange)):
                return False
    return True


def under_time_limit(kombinacija, interval):
    interval_trajanje = toMinutes(interval[1]) - toMinutes(interval[0])
    total_time = calculate_combo_duration(kombinacija)
    return total_time <= interval_trajanje


def calculate_interval_duration(interval):
    return toMinutes(interval[2]) - toMinutes(interval[1])


def calculate_combo_duration(kombinacija):
    return sum(calculate_interval_duration(p) for p in kombinacija)


def optimal(aktivnosti, interval):
    kombinacije = []
    for n in range(1, len(aktivnosti) + 1):
        kombinacije += [list(p) for p in itertools.combinations(aktivnosti, n)]

    tocne_komb = [k for k in kombinacije
                  if has_no_intersections(k) and under_time_limit(k, interval)]

    optimalna_kombinacija = []
    naj_trajanje_najduzeg = 0
    for k in tocne_komb:
        if len(k) > len(optimalna_kombinacija) or (len(k) == len(optimalna_kombinacija) and calculate_combo_duration(k) > naj_trajanje_najduzeg):
            naj_trajanje_najduzeg = calculate_combo_duration(k)
            optimalna_kombinacija = k

    return optimalna_kombinacija


aktivnosti = [
    ('F', (1, 10), (1, 20)),
    ('G', (1, 15), (1, 22)),
    ('A', (1, 12), (1, 14)),
    ('R', (1, 4), (1, 55)),
]

print(optimal(aktivnosti, ((0, 10), (1, 40))))
