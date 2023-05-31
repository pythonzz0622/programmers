# 효율성 개나줘버린 코드
def solution(topping):
    if len(set(topping)) % 2 == 1:
        return 0
    answer = 0
    for i  in range(1 , len(topping)):
        if (len(set(topping[:i])) == len(set(topping[:i]))):
            answer +=1



    return answer

# 효율생각한 다른사람 코드
def solution(topping):
    passed1 , passed2 = set() , set()
    check1 , check2 = [] , []
    for each in topping:
        passed1.add(each)
        check1.append(len(passed1))
    for each in topping[::-1]:
        passed2.add(each)
        check2.append(len(passed2))

    check2 = check2[::-1]
    return sum(1 for index in range(len(check1) - 1) if check1[index] == check2[index + 1 ])

# 효율생각한 다른사람 코드
from collections import Counter


def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    answer = 0
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer