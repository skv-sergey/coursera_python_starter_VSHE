from math import floor, ceil
n = float(input())
fraction = (n - int(n))
if fraction >= 0.5:
    rusRound = ceil(n)
elif fraction < 0.5:
    rusRound = floor(n)
print(rusRound)
