a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a == 0:
    print(0, e / b)
else:
    y = (f - (c * e) / a) / (d - ((c * b) / a))
    x = (e - b * y) / a
    print(x, y)
