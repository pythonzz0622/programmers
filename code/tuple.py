import ast
import re


## 프로그래머스 튜플문제
def solution(s):
    s = re.sub('{', '[', s)
    s = re.sub('}', ']', s)
    s = ast.literal_eval(s)
    n = len(s)
    answer = []
    number = []
    sort_dict = {}
    for i, s in enumerate(s):
        sort_dict[len(s)] = s

    for i in range(n):
        j = sort_dict[i + 1]
        for j_i in j:
            if j_i not in answer:
                answer.append(j_i)
    return answer

## 참고한 코드

def solution(s):
    s = s.replace('{' , '[').replace('}' ,"]")
    s = ast.literal_eval(s)
    answer = []
    s.sort(key= len)
    for s_i in s:
        for j_i in s_i:
            if j_i not in answer: answer.append(j_i)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))