from itertools import combinations as cmb
def solution(numbers):
    cmb_list = list(cmb(numbers , 2))
    answer= list(set([sum(cmb_i) for cmb_i in cmb_list]))
    answer.sort()
    return answer