def xor(x, y):
    if x == y:
        return 0
    else:
        return 1


x, y = int(input()), int(input())
print(xor(x, y))
