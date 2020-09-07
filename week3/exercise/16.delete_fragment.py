string = input()
pos = string.find('h')
reverse_pos = string[::-1]
pos_last = len(string) - (reverse_pos.find('h'))
print(string[:pos], string[pos_last:], sep='')
