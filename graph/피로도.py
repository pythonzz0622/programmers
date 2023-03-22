from itertools import permutations
c = 0 
def dfs(k , idx , dungeons):
    global c
    min_fat , con_fat = dungeons[idx]
    if k < min_fat:
        return
    else:
        k -= con_fat
        c += 1
        idx += 1
        if idx == len(dungeons):
            return 
        dfs(k , idx , dungeons)
        
def solution(k, dungeons): 
    answer = 0
    global c
    for dungeon in permutations(dungeons , len(dungeons)):
        c = 0
        dfs(k , 0 , dungeon)
        if answer < c:
            answer = c
    return answer


print(solution(80	,[[80,20],[50,40],[30,10]]))