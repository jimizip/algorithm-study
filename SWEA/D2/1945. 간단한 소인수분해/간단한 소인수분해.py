T = int(input())
for tc in range(1, T+1):
    n = int(input())
    
    # 각 소인수(2, 3, 5, 7, 11)의 지수를 저장할 리스트
    exp = []
    
    # 소인수 리스트
    primes = [2, 3, 5, 7, 11]
    
    # 각 소수로 나누어떨어지는 횟수 카운트
    for p in primes:
        cnt = 0
        while n % p == 0:  # n이 p로 나누어떨어지는 동안
            n //= p  # 몫 연산자(//): 나눈 후 정수 부분만 취함
            cnt += 1  # 지수 증가
        exp.append(cnt)
    
    # 결과 출력 (리스트를 공백으로 구분하여 출력)
    # *exp: 언패킹 연산자, [1,2,3] -> 1 2 3으로 변환
    print(f"#{tc}", *exp)
