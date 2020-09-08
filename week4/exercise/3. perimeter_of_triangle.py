def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())

print(dist(x1, y1, x2, y2) + dist(x3, y3, x2, y2) + dist(x1, y1, x3, y3))
