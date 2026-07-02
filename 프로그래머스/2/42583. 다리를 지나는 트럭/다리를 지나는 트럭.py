from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    tmp = 0
    while len(truck_weights)!=0:
        answer+=1

        tmp -= bridge.popleft()

        if tmp + truck_weights[0] <= weight:
            tmp+= truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    answer += bridge_length
    
    return answer