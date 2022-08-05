x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def IsPointInCircle(x, y, xc, yc, r):
    r_sq = r ** 2
    sum_eq = (xc - x) ** 2 + (yc - y) ** 2

    return ['NO', 'YES'][r_sq >= sum_eq]


print(IsPointInCircle(x, y, xc, yc, r))
