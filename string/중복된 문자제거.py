from collections import OrderedDict # 삽입된 순서대로 데이터를 획득할 수 있는 class
def solution(s):
    # 순서가 있는 중복 제거를 위해서
    string = list(OrderedDict.fromkeys(s))
    return string


def solution(s):
    string = list(s)
    answer = []
    
    while string:
        s_i = string.pop(0)
        if s_i not in answer:
            answer.append(s_i)

    return ''.join(answer )


print(solution("We are the world"))

