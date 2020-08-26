p, x, y = int(input()), int(input()), int(input())
deposit = x + (y / 100)
newDeposit = deposit * (p / 100 + 1)

roubles = int(newDeposit)
copeck = round((newDeposit - int(newDeposit)) * 100)
print(roubles, copeck)
