def MinDivisor(n):
    i = 2
    while n % i != 0:
        i += 1
    return i


n = int(input())
print(MinDivisor(n))
