if a <= b and a <= c:
    if b <= c:
        pass
    elif c <= b:
        b, c = c, b
elif b <= a and b <= c:
    if a <= c:
        a, b, = b, a
    elif c <= a:
        a, b, c = b, c, a
elif c <= a and c <= b:
    if a <= b:
        a, b, c = c, a, b
    elif b <= a:
        a, c = c, a