'''
Primjenom dinamičkog programiranja riješite zadatak 3 tako da neke aktivnosti
vrijede više od drugih. Tada bi cilj bio naći kombinaciju kompatibilnih aktivnosti
koja daje najveću moguću vrijednost. Na primjer, ako aktivnost F vrijedi 18, ak-
tivnost G vrijedi 2 i aktivnost A vrijedi 10, onda je najbolji odabir samo aktivnost
F jer je vrijednost tada 18, dok je sa A i G ukupna vrijednost 12.
'''


import itertools


def toMinutes(interval):
    sati, minute = interval
    return sati * 60 + minute


def convertToRange(interval):
    return range(toMinutes(interval[1]), toMinutes(interval[2]))


def has_no_intersections(kombinacija):
    L = len(kombinacija)
    for i in range(0, L):
        nrange = convertToRange(kombinacija[i])
        for j in range(i+1, L):
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


def calculate_combo_value(kombinacija):
    return sum(p[3] for p in kombinacija)


def optimal(aktivnosti, interval):
    kombinacije = []
    for n in range(1, len(aktivnosti) + 1):
        kombinacije += [list(p) for p in itertools.combinations(aktivnosti, n)]
    tocne_komb = [k for k in kombinacije
                  if has_no_intersections(k) and under_time_limit(k, interval)]

    optimalna_kombinacija = []
    naj_vrijednost = 0
    for k in tocne_komb:
        vrijednost = calculate_combo_value(k)
        if vrijednost > naj_vrijednost:
            naj_vrijednost = vrijednost
            optimalna_kombinacija = k
        elif vrijednost == naj_vrijednost and len(k) > len(optimalna_kombinacija):
            optimalna_kombinacija = k

    return optimalna_kombinacija


aktivnosti = [
    ('F', (1, 10), (1, 20), 18),
    ('G', (1, 15), (1, 22), 2),
    ('A', (1, 12), (1, 14), 15),
    ('R', (1, 4), (1, 55), 4),
]

print(optimal(aktivnosti, ((1, 00), (1, 20))))
