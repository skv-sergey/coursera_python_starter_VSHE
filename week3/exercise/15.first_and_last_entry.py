string = input()
pos = string.find('f')
if pos == -1:
    pass
elif string.find('f', pos + 1) == -1:
    print(string.find('f'))
else:
    reverse = string[::-1]
    pos_last = len(string) - (reverse.find('f') + 1)
    print(string.find('f'), string.find("f", pos_last))
