n = int(input())
hour = (n // 3600) % 24
mMajor = ((n // 60) % 60) // 10
mMinor = ((n // 60) % 60) % 10
sMajor = (n % 60) // 10
sMinor = (n % 60) % 10
print(hour, ":", mMajor, mMinor, ":", sMajor, sMinor, sep="")
