string = input()
pos = string.find(' ')
print(string[pos + 1:], string[:pos])
