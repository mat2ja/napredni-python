import math

cijene = {
    1: 1,
    2: 5,
    3: 8,
    4: 9,
    5: 10,
    6: 17,
    7: 17,
    8: 20,
    9: 24,
    10: 30
}


def opt_vr(cjenik, n):
    if n == 0:
        return 0
    else:
        q = -math.inf
        for i in range(1, n + 1):
            q = max(q, cjenik[i] + opt_vr(cjenik, n - i))
    return q


def opt_vr_memo(cjenik, n, memo={}):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    else:
        q = -math.inf
        for i in range(1, n + 1):
            q = max(q, cjenik[i] + opt_vr(cjenik, n - i))
    memo[n] = q
    return q


def optimum_rek(cjenik, d):
    def f(n, k, tab=' '):
        """
        n: duljina cijevi
        k: trenutna kombinacija
        """
        if n == 0:
            print(f'{tab }{k} -> {n}')
            return (0, [])
        else:
            print(f'{tab }{k} -> {n}')
            m = (-math.inf, [])  # lokalni maksimum
            for i in range(1, n + 1):
                m = max(m,
                        (cjenik[i] + f(n - i, k + [i], tab + (' ' * 4))[0],
                         k + [i] + [n - i]))
                print(f'{"." * len(tab)}{k} -> {n} = ${m[0]} ')
            return m
    return f(d, [])


# print(optimum_rek(cijene, 4))
print(opt_vr_memo(cijene, 4))
