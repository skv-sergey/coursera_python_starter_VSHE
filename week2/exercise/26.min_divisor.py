n = int(input())
minDiv = int(2)
while n % minDiv != 0:
    minDiv = minDiv + 1
print(minDiv)
