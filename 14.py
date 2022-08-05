def GCD(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        R = max(a, b) % min(a, b)
        return GCD(min(a, b), R)


x = int(input())
n = int(input())
print(GCD(x, n))
