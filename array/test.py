string = 'level'
c = 0 
full = len(string)
for i in range(len(string)):
    if string[i] == string[-i-1]:
        c +=1
if c == full:
    print(c)
    print('clear')
