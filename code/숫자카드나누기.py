## 이 함수 몰라서 효율성이 안나와서 통과못함
from math import gcd


# 리스트 내 최대 공약수 구해줌
def get_gcd(arr):
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])
    return g


def solution(arrayA, arrayB):
    # 첫 번째 조건, 두 번째 조건 둘다 아닐때
    res = 0

    # 최대공약수 가져옴
    A, B = get_gcd(arrayA), get_gcd(arrayB)

    # 첫 번째 조건
    for i in arrayB:
        if i % A == 0:
            break
    else:
        res = max(A, res)
    # 두 번째 조건
    for i in arrayA:
        if i % B == 0:
            break
    else:
        res = max(B, res)

    return res