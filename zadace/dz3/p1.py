# imperativan nacin

def datum(s):
    dijelovi = s.split('.')
    if len(dijelovi) != 4:
        return False
    for e in dijelovi[:-1]:
        print(e)
        if not e.isnumeric():
            return False
    return dijelovi[-1] == ''


print(datum('4.12.2019.2'))
