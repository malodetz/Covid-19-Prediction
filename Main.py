# Zhuravlev Sergej, 2020a
# Covid-19 prediction
# 09.05.2020
from math import sqrt

from Gauss import solve


def calcpairsum(i, j, x, k):
    s = 0
    for idx in range(k, len(x)):
        s += x[idx - i] * x[idx - j]
    return s


def calcsum(i, x, k):
    s = 0
    for idx in range(k, len(x)):
        s += x[idx - i]
    return s


def buildmatrix(x, k, with_const=False):
    if with_const:
        m = [[0] * (k + 2) for _ in range(k + 1)]

        m[-1][-1] = calcsum(0, x, k)
        for i in range(k):
            m[-1][i] = calcsum(i + 1, x, k)
            m[i][k] = m[-1][i]
        m[k][k] = 1
    else:
        m = [[0] * (k + 1) for _ in range(k)]

    for i in range(k):
        m[i][-1] = calcpairsum(0, (i + 1), x, k)
        for j in range(k):
            m[i][j] = calcpairsum((i + 1), (j + 1), x, k)

    return m


def predict(x, k, f, n, with_const=False):
    ans = [0] * n
    for i in range(n):
        for j in range(k):
            ans[i] += x[len(x) - 1 - j] * f[j]
        if with_const:
            ans[i] += f[-1]
        ans[i] = int(ans[i])
        x.append(ans[i])
    return ans


def experiment():
    for k in range(1, 20):
        for flag in [False, True]:
            tr = train.copy()
            f = solve(buildmatrix(tr, k, flag))
            predicted = predict(tr, k, f, m, flag)
            print("For k = " + str(k), end="")
            if flag:
                print(" with constant factor:")
            else:
                print(":")
            print("    Predicted values: ", *predicted)
            d = sqrt(sum((predicted[i] - test[i]) ** 2 for i in range(m)) / m)
            print("    Standard deviation: ", d)


fin = open("data.txt", "r")
n = int(fin.readline())
train = [int(fin.readline()) for _ in range(n)]
m = int(fin.readline())
test = [int(fin.readline()) for _ in range(m)]
print("Real values: ", *test)
experiment()
