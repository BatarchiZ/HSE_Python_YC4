def Phib(n):
    if n == 0:
        return (0)
    if n == 1:
        return (1)
    else:
        return Phib(n - 1) + Phib(n - 2)


x = int(input())
print(Phib(x))
