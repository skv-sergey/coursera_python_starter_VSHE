n = int(input())
major1 = n // 1000
minor1 = (n // 100) % 10
major2 = (n // 10) % 10
minor2 = n % 10
number1 = str(major1) + str(minor1)
number2 = str(minor2) + str(major2)
number1 = int(number1)
number2 = int(number2)
print(number1 - number2 + 1)
