import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x = abs(x1 - x2)
y = abs(y1 - y2)

sqx = x ** 2
sqy = y ** 2

ans = math.sqrt(sqx + sqy)

print(ans)
