from collections import Counter
def solution(id_list, report, k):
    report = list(set(report))
    report = [report_i.split(' ') for report_i in report]
    counter = Counter([report_i[1] for report_i in report])
    id_dict = {id_list_i : 0 for id_list_i in id_list}
    for report_i in report:
        if counter[report_i[1]] >= k:
            id_dict[report_i[0]] += 1

    return list(id_dict.values())


print(solution(["muzi", "frodo", "apeach", "neo"],	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))