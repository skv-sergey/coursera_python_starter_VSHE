n = int(input())
max1 = n
max2 = 0
while n != 0:
    n = int(input())
    if max1 <= n != 0:
        max2 = max1
        max1 = n
    elif max2 < n < max1:
        max2 = n

print(max2)
