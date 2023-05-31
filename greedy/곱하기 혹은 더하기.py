num = '567'
num = list(map(int , list(num)))
print(num)

def is_0_1(x):
    if x == 0 or x == 1:
        return True
    else:
        return False

x = num[0]
for num_i in num[1:]:
    if is_0_1(x) or is_0_1(num_i):
        x = x + num_i
    else:
        x = x * num_i
print(x)

# 정답
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1 , len(data)):
    # 두 수 중에서 하나라도 0 혹은 1 인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)