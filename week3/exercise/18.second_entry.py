string = input()
pos = string.find('f')
if pos == -1:
    print('-2')
elif string.find('f', pos + 1) == -1:
    print('-1')
else:
    print(string.find('f', pos + 1))
