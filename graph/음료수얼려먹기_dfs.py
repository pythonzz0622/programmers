from collections import deque
data = '''00110
00011
11111
00000'''

N = 4 
M =5 
data = [[int(data_j) for data_j in data_i] for data_i in data.split('\n')]


def dfs(y,x):
    global N 
    global M 
    global data 

    if y >= N or y <= -1 or x >= M or x <= -1 or data[y][x] == 1:
        return False
    
    data[y][x] = 1
    dfs(y-1 , x )
    dfs(y+1 , x)
    dfs(y , x-1)
    dfs(y , x +1)

    return True

c = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            c += dfs(i , j)

print(c)
