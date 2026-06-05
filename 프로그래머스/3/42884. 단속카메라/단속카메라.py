def solution(routes):
    routes.sort()
    current = routes[0]
    answer = 1
    
    for i in range(1, len(routes)):
        if routes[i][1] <= current[1]:
            current[1] = routes[i][1]
        if routes[i][0] <= current[1]:
            current[0] = routes[i][0]
        else:
            current = routes[i]
            answer += 1
    
    return answer