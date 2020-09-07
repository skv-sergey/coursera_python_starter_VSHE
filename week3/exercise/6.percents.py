p, x, y = int(input()), int(input()), int(input())
deposit = x * 100 + y
total = deposit * (p / 100) + deposit

print(int(total // 100), int(total % 100))
