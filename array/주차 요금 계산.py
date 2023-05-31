import math
def cvt_miniutes(time):
    time = list(map(int , time.split(':')))
    return time[0] * 60 + time[1]

def cal_fees(time , per_minutes , per_fee , base_time , base_fee):
    if time <= base_time:
        return base_fee
    return base_fee + math.ceil((time - base_time) / per_minutes) * per_fee

def solution(fees, records):
    base_time , base_fee , per_minutes , per_fee = fees 
    records = [record.split(' ')for record in records]
    records = sorted(records , key = lambda x : x[1])
    id_set = {record[1] : 0 for record in records}
    
    for id_set_i in id_set.keys():
        single_record = [record for record in records if record[1] in id_set_i]
        if len(single_record) % 2:
            single_record.append(["23:59" , id_set_i , 'OUT'])

        in_time_list = [s_r[0] for s_r in single_record if s_r[2] == 'IN']
        out_time_list = [s_r[0] for s_r in single_record if s_r[2] == 'OUT']
        result = 0
        for i in range(len(in_time_list)):
            result += cvt_miniutes(out_time_list[i]) - cvt_miniutes(in_time_list[i]) 
        
        id_set[id_set_i] = cal_fees(result , per_minutes , per_fee , base_time , base_fee)
            
            

    return list(id_set.values())