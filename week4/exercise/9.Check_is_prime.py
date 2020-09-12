def IsPrime(n):
    i = 2
    j = 0
    if n == 2 or n == 3:
        return True
    while i <= n:
        if i * i <= n and j != 1:
            if n % i == 0:
                j = 1
                i += 1
            else:
                i += 1
        else:
            if j == 1:
                return False
            else:
                return True


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
