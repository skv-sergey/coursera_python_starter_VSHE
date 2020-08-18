if a2 <= b2 and a2 <= c1:
    if b2 <= c1:
        pass
    elif c1 <= b2:
        b2 = b1
        b2, c1 = c1, b2
elif b2 <= a2 and b2 <= c1:
    if a2 <= c1:
        a2, b2, = b2, a2
    elif c1 <= a2:
        a2, b2, c = b2, c1, a2
elif c1 <= a2 and c1 <= b2:
    if a2 <= b2:
        a2, b2, c1 = c1, a2, b2
    elif b2 <= a2:
        a2, c1 = c1, a2
