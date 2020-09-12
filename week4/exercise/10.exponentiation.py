def power(a, n):
    if n == 0:
        return 1
    n -= 1
    if n < 1:
        return a
    return a * power(a, n)


a, n = float(input()), int(input())
print(power(a, n))
