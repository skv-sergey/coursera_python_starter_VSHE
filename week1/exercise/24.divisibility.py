a = int(input())
b = int(input())
z = 0 ** (a % b)
print("YES" * z, "NO" * (0 ** z), sep="")
