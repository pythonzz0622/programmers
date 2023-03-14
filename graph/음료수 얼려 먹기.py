from collections import deque
data = '''00110
00011
11111
00000'''

N = 4 
M =5 
data = [[int(data_j) for data_j in data_i] for data_i in data.split('\n')]

dy = [0, -1 , 0 , 1]
dx = [-1, 0 , 1, 0]
def is_in( y,x):
    global N
    global M
    data_y = [dy_i + y for dy_i in dy]
    data_x = [dx_i + x for dx_i in dx]
    data_offeset = [[y , x] for y , x in zip(data_y , data_x) if y > -1 and x  >-1 and y < N and x < M]
    return data_offeset

c =0
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            data[i][j] == 1
            queue = [[i,j]]

            while queue:
                y,x = queue.pop(0)
                data_offset = is_in( y , x)
                for temp_y , temp_x in data_offset:
                    if data[temp_y][temp_x] == 0:
                        data[temp_y][temp_x] = 1
                        queue.append([temp_y,temp_x])
            
            c +=1
            
print(c)
print(data)

