a, b, c = int(input()), int(input()), int(input())
# a, b, c = int(1), int(1), int(1)
if a == b and b == c:
    print(3)
elif a == b or b == c or c == a:
    print(2)
else:
    print(0)
