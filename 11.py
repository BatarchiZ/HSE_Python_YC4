import sys

sys.setrecursionlimit(1000000)

a = float(input())
n = float(input())


def Power(a, n):
    if n == 0:
        return 1
    if n > 0:
        return a * Power(a, n - 1)
    if n < 0:
        return 1 / a * Power(a, n + 1)


print(Power(a, n))
