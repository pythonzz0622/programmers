def get_range(range_i, data):
    return range_i[0], len(data) + range_i[1] -1


def solution(k, ranges):
    answer = []

    answer.append(k)
    while k != 1:
        if k % 2 == 0:
            k /= 2
            answer.append(k)
        else:
            k = k * 3 + 1
            answer.append(k)

    data = []
    try:
        for i in range(len(answer)):
            data.append((answer[i] + answer[i + 1]) / 2)
    except IndexError:
        data.append(-1)

    result_list = []
    for range_i in ranges:
        if range_i == [0, 0]:
            result_list.append(sum(data[:-1]))
            continue
        else:
            range_i = get_range(range_i , data)
            re = 0
            if range_i[0] > range_i[1]:
                result_list.append(-1.0)
                continue
            for j in range(range_i[0], range_i[1]):
                re += data[j]
            result_list.append(re)

    return result_list