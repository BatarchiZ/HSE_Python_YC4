def Exponent(a, n):
    if n == 1:
        return a
    else:
        if n % 2 == 0:
            return (a ** 2) ** (n / 2)
        if n % 2 != 0:
            return a * (a ** 2) ** ((n - 1) / 2)


x = float(input())
n = float(input())
print(Exponent(x, n))
