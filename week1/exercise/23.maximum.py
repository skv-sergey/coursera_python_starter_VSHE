a = int(input())
b = int(input())
z = (a * (a // b) + b * (b // a))
print(z // ((a // b) + (b // a)))
