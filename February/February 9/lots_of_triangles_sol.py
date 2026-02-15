import cmath

MAXN = 400

def cross(a, b):
    return (a.conjugate() * b).imag

def get_point():
    x, y = map(int, input().split())
    return complex(x, y)

def below(i, j):
    return lis[i].real == lis[j].real and lis[i].imag < lis[j].imag

def between_below(i, j, x):
    if lis[i].real < lis[j].real:
        return (lis[i].real < lis[x].real < lis[j].real and
                cross(lis[j] - lis[i], lis[x] - lis[i]) < 0)
    else:
        return (lis[j].real < lis[x].real < lis[i].real and
                cross(lis[i] - lis[j], lis[x] - lis[j]) < 0)

with open("triangles.in") as fin:
    n = int(fin.readline())
    lis = [complex(*map(int, fin.readline().split())) for _ in range(n)]

num = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if lis[i].real < lis[j].real:
            for k in range(n):
                if k != i and k != j:
                    if below(k, i):
                        num[i][j] += 1
                    if below(k, j):
                        num[i][j] += 1
                    if between_below(i, j, k):
                        num[i][j] += 2
            num[j][i] = -num[i][j]

ans = [0]*(n-2)
for i in range(n):
    for j in range(i):
        for k in range(j):
            temp = abs(num[i][j] + num[j][k] + num[k][i]) // 2
            temp -= between_below(i, j, k)
            temp -= between_below(j, k, i)
            temp -= between_below(k, i, j)
            ans[temp] += 1

with open("triangles.out", "w") as fout:
    for i in range(n-2):
        fout.write(str(ans[i]) + "\n")