import sys

sys.setrecursionlimit(20000)


def Sum(x, y):
    if y == 0:
        return x
    else:
        return x + int(Sum(1, y - 1))


a = int(input())
n = int(input())

print(Sum(a, n))
