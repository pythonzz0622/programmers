string = 'AJKDLSI412K4JSJ9D'
string = sorted(string)
num = 0 
str_j = ''
for str_i in string:
    if not str_i.isalpha():
        num += int(str_i)
    else:
        str_j += str_i

print(str_j + str(num))
    
# 정답
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

if value != 0:
    result.append(str(value))

print(''.join(result))