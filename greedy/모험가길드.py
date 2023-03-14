from collections import deque
N = 5
fear = map(int , '2 3 1 2 2'.split())
fear = sorted(fear)
print(fear)
user_list = deque(fear)
group_num = 0


while user_list: # user list가 빌때까지 iteration
    group = []
    u = user_list.popleft()
    group.append(u)
    while len(group) < max(group): # 그룹 인원수 < 그룹내 최대 공포도 
        try:
            u = user_list.popleft() # 
            group.append(u)
        except IndexError:
            break # 데이터 비었을때 stop
        
    if len(group) == max(group):
        group_num += 1

print(group_num)

## 정답

result = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모험가 수
data = [1,2,2,2,3]
for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count +=1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
print(result)