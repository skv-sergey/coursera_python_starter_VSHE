def power(a, n):
    if n == 0:
        return 1

    elif n > 0:
        b = a
        while n > 1:
            b = b * a
            n -= 1
        return b

    elif n < 0:
        n = -n
        b = a
        while n > 1:
            b = b * a
            n -= 1
        return 1 / b


a, n = float(input()), int(input())
print(power(a, n))
