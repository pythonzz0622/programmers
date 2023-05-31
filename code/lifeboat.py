from itertools import combinations
def solution(elements):
    answer = []
    for i in range(1, len(elements) + 1):
        answer.extend([sum(i) for i in list(set(list(combinations(elements ,i ))))])
    answer = len(set(answer))
    return answer



print(solution([7,9,1,1,4]))