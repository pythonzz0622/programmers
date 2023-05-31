from collections import Counter
def solution(k, tangerine):
    answer = 0
    value = list(Counter(tangerine).items())
    value.sort(key = lambda x : x[1] , reverse = True)
    c = 0
    for value_i in value:
        if value_i[1] + c >= k:
            answer += 1
            break
        else:
            c += value_i[1]
            answer +=1
    return answer