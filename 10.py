n = int(input())


def IsPrime(x):
    if x == 2:
        return 'YES'
    if x == 5:
        return 'YES'
    if x == 7:
        return 'YES'
    if x % 2 == 0:
        return 'NO'
    if x == 3:
        return 'YES'
    for x in range(3, int(n ** (1 / 2) + 1), 2):
        if n % x == 0:
            return 'NO'
    else:
        return 'YES'


print(IsPrime(n))
