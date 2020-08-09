n = int(input())
hour = (n // 3600) % 24
minute = (n // 60) % 60
second = n % 60
print(hour, ":", minute, ":", second, sep="")
