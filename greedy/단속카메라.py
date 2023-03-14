def solution(routes):
    routes.sort(key = lambda x : x[0])
    # print(routes)
    lt , rt = routes[0]
    c = 1
    for route in routes[1:]:
        if route[0] <= rt:
            lt = max(lt , route[0])
            rt = min(route[1] , rt)
        else:
            lt , rt = route
            c += 1
        
    return c


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	))