str_to_int = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 
              'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

int_list = '0123456789'
def solution(s):
    answer = ''
    num_str = ''
    string = list(s)
    while string:
        i = string.pop(0)

        if i in int_list:
            answer += i
        else:
            num_str += i 
            if num_str in str_to_int.keys():
                answer += str(str_to_int[num_str])
                num_str = ''

    return answer

print(solution("one4seveneight"))