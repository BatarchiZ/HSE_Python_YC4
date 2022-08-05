import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

xl1 = abs(x1 - x2)
yl1 = abs(y1 - y2)
xl2 = abs(x2 - x3)
yl2 = abs(y2 - y3)
xl3 = abs(x3 - x1)
yl3 = abs(y3 - y1)

sqx1 = xl1 ** 2
sqy1 = yl1 ** 2

sqx2 = xl2 ** 2
sqy2 = yl2 ** 2

sqx3 = xl3 ** 2
sqy3 = yl3 ** 2

ans1 = math.sqrt(sqx1 + sqy1)
ans2 = math.sqrt(sqx2 + sqy2)
ans3 = math.sqrt(sqx3 + sqy3)
p = ans1 + ans2 + ans3
print('{0:.10f}'.format(p))
