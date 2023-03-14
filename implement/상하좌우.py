N = 5
plan = 'R R R U D D'
plan = plan.split(' ')
print(plan)

USER = [1,1]

def movement(pos , move):
    y = pos[0] + move[0]
    x = pos[1] + move[1]
    return [y , x]

def error_filter(pos , move , N):
    y , x = movement(pos , move)
    if (x < 1) or (x > N) or (y < 1) or (y > N): return pos

    else: return y, x

go = {'L' : [0 , -1], 'R' : [0 , 1], 'U' : [-1 , 0], 'D' : [1 , 0]}

for plan_i in plan:
    move = go[plan_i]
    USER = error_filter(USER , move , N)

print(USER)


# 해설
dx = [0, 0, -1 ,1]
dy = [-1 ,1 ,0 ,0]
move_types = ['L', 'R' ,'U' , 'D']
plans = plan
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx <1 or ny < 1 or nx > N or ny > N:
            continue
        x ,y = nx , ny
