n = int(input())
unit = n % 10
dozen = (n // 10) % 10
hundred = (n // 100) % 100
print(unit + dozen + hundred)
