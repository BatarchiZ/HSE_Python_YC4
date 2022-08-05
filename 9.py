n = int(input())


def MinDivisor(n):
    if n % 2 == 0:
        return 2
    for a in range(3, int(n ** (1 / 2) + 1), 2):
        if n % a == 0:
            return a
    else:
        return n


print(MinDivisor(n))
