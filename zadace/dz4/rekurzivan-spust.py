def rekurzivan_spust(niz):
    i = 0

    def S(niz):
        nonlocal i
        if niz[i] == 'a':  # recenica moze poceti s "a"
            i += 1
            if not S(niz):  # nakon "a" slijedi S
                return False

            # Nakon S mora slijediti "b" (zato se ovo
            # nalazi nakon rekurzivnog poziva za S).
            if niz[i] != 'b':
                return False
            else:
                i += 1
        else:  # recenica moze poceti sa "x"
            if niz[i] != 'x':
                return False
            else:
                i += 1
        return True

    try:
        r = S(niz)
        if i >= len(niz):
            return r
        else:
            return False
    except Exception:
        return False


# print(rekurzivan_spust('aaxbb'))
print(rekurzivan_spust('aaxbbb'))
