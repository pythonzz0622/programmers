N = input()

split = len(N) // 2 

def cal(x):
    result = 0 
    for x_i in x:
        result += int(x_i)
    return result

if cal(N[:split]) == cal(N[split:]):
    print('LUCKY')
else:
    print('READY')
