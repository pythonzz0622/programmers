from collections import deque

def is_true(data):
    stack = []
    data_list = data.copy()
    while data_list:
        v = data_list.pop(0)
        if v == "(" or v == "[" or v == "{":
            stack.append(v)
        else:
            if v == ')':
                if '(' in stack:
                    stack.remove('(')
                else:
                    return False

            if v == ']':
                if '[' in stack:
                    stack.remove('[')
                else:
                    return False

            if v == '}':
                if '{' in stack:
                    stack.remove('{')
                else:
                    return False

    if stack == []:
        return True
    else:
        return False


def solution(s):
    answer = 0
    data = list(s)
    for i in range(len(data)):
        answer += is_true(data)
        l = data.pop(0)
        data.append(l)

    return answer

"([{)}]"