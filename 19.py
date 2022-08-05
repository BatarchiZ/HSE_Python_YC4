import sys

sys.setrecursionlimit(1000000)


def Reverse():
    n = input()

    if n == '0':
        return ''
    if n == '':
        return Reverse()
    if float(n) < 0:
        return Reverse()
    else:
        return Square(n)


def Square(n):
    if (float(n) ** (1 / 2)) % 1 == 0:
        return Reverse() + ' ' + n
    else:
        return Reverse()


x = Reverse()
if len(x) == 0:
    print(0)
else:
    print(x)
