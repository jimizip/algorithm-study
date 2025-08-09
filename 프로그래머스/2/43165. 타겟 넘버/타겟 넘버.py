from collections import deque

def solution(numbers, target):
    
    answer = 0
    
    queue = deque()
    # 시작 상태: (누적 합 0, 0번 인덱스부터 시작)
    queue.append((0, 0))

    while queue:
        # 현재 상태(누적 합, 인덱스)를 꺼냄
        current_sum, index = queue.popleft()
        
        # 종료: 모든 숫자를 다 사용했을 때 (현재 인덱스가 배열 길이와 같을 때)
        if index == len(numbers):
            # 누적 합이 타겟 넘버와 일치하는지 확인
            if current_sum == target:
                # 일치하면 방법의 수를 1 증가
                answer += 1
        else:
            # 현재 인덱스의 숫자를 가져옴
            current_number = numbers[index]
            
            # 현재 숫자를 더하는 경우
            # (현재 누적 합 + 현재 숫자, 다음 인덱스)를 큐에 추가
            queue.append((current_sum + current_number, index + 1))
            
            # 현재 숫자를 빼는 경우
            # (현재 누적 합 - 현재 숫자, 다음 인덱스)를 큐에 추가
            queue.append((current_sum - current_number, index + 1))
            
    return answer
