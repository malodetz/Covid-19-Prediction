# Zhuravlev Sergej, 2020a
# Solving a system of linear equations
# 14.04.20

EPS = 10 ** (-9)


def solve(a, mode=False):
    n = len(a)
    for i in range(n):
        if abs(a[i][i]) <= EPS:
            pos = -1
            for j in range(i, n):
                if abs(a[j][i]) > EPS:
                    pos = j
                    break
            bad = True
            for j in range(n):
                if abs(a[i][j]) > EPS:
                    bad = False
                    break
            if not bad:
                continue
            assert (abs(a[i][-1]) <= EPS), "System has no solution."
            assert (pos != -1), "System has multiple solutions."
            a[i], a[pos] = a[pos], a[i]
        d = a[i][i]
        for j in range(n + 1):
            a[i][j] /= d
        for j in range(n):
            if j == i:
                continue
            d = a[j][i]
            for k in range(n + 1):
                a[j][k] -= a[i][k] * d
    for i in range(n):
        bad = True
        for j in range(n):
            if abs(a[i][j]) > EPS:
                bad = False
                break
        if not bad:
            continue
        assert (abs(a[i][-1]) <= EPS), "System has no solution."
    if mode:
        for i in range(n):
            print(*a[i])
    ans = [a[i][-1] for i in range(n)]
    return ans
