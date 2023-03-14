def solution(gems):
    flag = False
    gem_counter = {gem : 0 for gem in set(gems)}
    all_gems_count = len(gem_counter.keys())
    for i, gem in enumerate(gems):
        if flag: break
        gem_counter[gem] += 1
        is_true = list(map(bool , gem_counter.values()))
        if sum(is_true) == all_gems_count:
            end = i 
            for j , gem in enumerate(gems):
                gem_counter[gem] -= 1
                is_true = list(map(bool , gem_counter.values()))
                if sum(is_true) < all_gems_count:
                    start = j
                    flag = True
                    break



            
    return [start +1  ,  end + 1]


import collections
def solution(gems):
    answer = [0, 0]
    sH = collections.defaultdict(int)
    k = len(set(gems))
    lt = 0 
    maxL = 1000000
    for rt in range(len(gems)):
        sH[gems[rt]] +=1
        while len(sH) ==k :
            if rt-lt+1 < maxL:
                maxL = rt-lt+1
                answer = [lt+1, rt+1]
            sH[gems[lt]] -=1
            if sH[gems[lt]] == 0:
                del sH[gems[lt]]
            lt +=1
                
    return answer
            


print(solution(["A", "B", "B", "B", "C", "D", "D", "D", "D", "D", "D", "D", "B", "C"]))