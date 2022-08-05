n = int(input())
k = int(input())


def Factorial(x):
    if x < 1:
        return 1
    else:
        return x * Factorial(x - 1)


answer = Factorial(n) / (Factorial(k) * Factorial(n - k))
print(int(answer))
