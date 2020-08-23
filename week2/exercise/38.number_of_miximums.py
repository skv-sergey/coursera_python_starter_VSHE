n = int(input())
max1 = n
i = 1
while n != 0:
    n = int(input())
    if max1 < n:
        max1 = n
        i = 1
    elif max1 == n:
        i += 1

print(i)
