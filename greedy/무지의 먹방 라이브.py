def solution(food_times, k):
    times = 0
    while food_times:
        times += min(food_times) * len(food_times)
        food_times = [food_time - min(food_times) for food_time in food_times]
        food_times = [food_time for food_time in food_times if food_time != 0]
    return times

food_times = [3,1,2]
k = 5

print(solution(food_times , k))