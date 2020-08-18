a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a1 <= b1 and a1 <= c1:
    if b1 <= c1:
        pass
    elif c1 <= b1:
        b1, c1 = c1, b1
elif b1 <= a1 and b1 <= c1:
    if a1 <= c1:
        a1, b1, = b1, a1
    elif c1 <= a1:
        a1, b1, c1 = b1, c1, a1
elif c1 <= a1 and c1 <= b1:
    if a1 <= b1:
        a1, b1, c1 = c1, a1, b1
    elif b1 <= a1:
        a1, c1 = c1, a1

if a2 <= b2 and a2 <= c2:
    if b2 <= c2:
        pass
    elif c2 <= b2:
        b2, c2 = c2, b2
elif b2 <= a2 and b2 <= c2:
    if a2 <= c2:
        a2, b2, = b2, a2
    elif c2 <= a2:
        a2, b2, c2 = b2, c2, a2
elif c2 <= a2 and c2 <= b2:
    if a2 <= b2:
        a2, b2, c2 = c2, a2, b2
    elif b2 <= a2:
        a2, c2 = c2, a2

if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
