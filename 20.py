n = int(input())

x = 1
a = 2
y = 3


def Move(n, x, y):
    mas = [1, 2, 3]
    mas.pop(mas.index(x))
    mas.pop(mas.index(y))
    if n == 1:
        print(n, x, y)
    else:
        Move(n - 1, x, mas[0])
        print(n, x, y)
        Move(n - 1, mas[0], y)


Move(n, x, y)
