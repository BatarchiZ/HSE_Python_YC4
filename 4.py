x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    answer = 'NO'
    if abs(x) <= 1:
        if abs(y) <= 1:
            answer = 'YES'
    return answer


print(IsPointInSquare(x, y))
