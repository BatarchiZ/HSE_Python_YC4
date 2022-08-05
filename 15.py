def ReduceFraction(a, b):
    if b == 0:
        return a
    else:
        R = a % b
        return ReduceFraction(b, R)


x = int(input())
n = int(input())
if x % n == 0:
    print(int(x / n), 1)
else:
    if int(ReduceFraction(x, n)) == 1:
        print(x, n)
    else:
        p = x / int(ReduceFraction(x, n))
        q = int(ReduceFraction(x, n))
        print(int(p), int(n / q))
