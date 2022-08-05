def Reverse():
    n = input()
    if n == '0':
        return '0'
    else:
        return Reverse() + '\n' + n


print(Reverse())
