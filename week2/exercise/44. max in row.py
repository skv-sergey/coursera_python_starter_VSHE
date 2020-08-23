n = int(input())
previous = n
i = 1
iMax = 1
while n != 0:
    n = int(input())
    if previous == n:
        i += 1
        if i >= iMax:
            iMax = i
    else:
        i = 1
        previous = n

print(iMax)
