x = float(input())
y = float(input())


def UseInAnArea(x, y):
    return ['NO', 'YES'][((x + 1) ** 2 + (y - 1) ** 2 >= 4 and (y <= 2 * x + 2) and y <= -x) or \
                         ((x + 1) ** 2 + (y - 1) ** 2 <= 4 and y >= -x and y >= 2 * x + 2)]


print(UseInAnArea(x, y))
