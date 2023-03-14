from collections import Counter
def solution(s):
    answer = dict(filter(lambda x : x[1] <=1 , Counter(list(s)).items()))
    answer= sorted(answer.keys())
    return ''.join(answer)