x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    answer = 'NO'
    if y <= x + 1 and y <= -x + 1 and y >= -x - 1 and y >= x - 1:
        answer = 'YES'
    return answer


print(IsPointInSquare(x, y))
