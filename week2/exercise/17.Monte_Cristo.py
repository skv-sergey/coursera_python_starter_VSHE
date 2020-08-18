a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
# a, b, c, d, e = int(1), int(1), int(1), int(1), int(1)
if a <= b and a <= c:
    if b <= c:
        a, b = a, b
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
else:
    pass
if d >= e and d >= b and e >= a:
    print("YES")
elif e >= d and e >= b and d >= a:
    print("YES")
else:
    print("NO")
