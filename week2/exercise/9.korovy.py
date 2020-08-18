a = int(input())
if a % 10 == 1 and a != 11:
    print(a, ' korova')
elif (a % 10 == 2 or a % 10 == 3 or a % 10 == 4) and (a // 10 != 1):
    print(a, ' korovy')
else:
    print(a, 'korov')
