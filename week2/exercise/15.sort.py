a, b, c = int(input()), int(input()), int(input())
# a, b, c = int(3), int(1), int(2)
if a <= b and a <= c:
    if b <= c:
        print(a, b, c)
    elif c <= b:
        b, c = c, b
        print(a, b, c)
elif b <= a and b <= c:
    if a <= c:
        a, b, = b, a
        print(a, b, c)
    elif c <= a:
        a, b, c = b, c, a
        print(a, b, c)
elif c <= a and c <= b:
    if a <= b:
        a, b, c = c, a, b
        print(a, b, c)
    elif b <= a:
        a, c = c, a
        print(a, b, c)
