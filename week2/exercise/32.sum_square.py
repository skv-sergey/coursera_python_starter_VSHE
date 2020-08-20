n = int(input())
i = int(1)
sum = 0
while i <= n:
    sum = i ** 2 + sum
    i += 1
print(sum)
