a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
D = (a * d) - (b * c)
D1 = (e * d) - (b * f)
D2 = (a * f) - (e * c)
print(D1 / D, D2 / D)
