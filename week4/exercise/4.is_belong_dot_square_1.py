def IsPointInSquare(x, y):
    return abs(max(abs(x), abs(y))) <= 1


x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
