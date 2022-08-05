a = float(input())
n = int(input())


def Power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    else:
        return a * Power(a, n - 1)


print(Power(a, n))
