T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = []
    two = 0
    three = 0
    five = 0
    seven = 0
    eleven = 0

    while N % 2 == 0:
        N /= 2
        two += 1
    result.append(two)
    while N % 3 == 0:
        N /= 3
        three += 1
    result.append(three)
    while N % 5 == 0:
        N /= 5
        five += 1
    result.append(five)
    while N % 7 == 0:
        N /= 7
        seven += 1
    result.append(seven)
    while N % 11 == 0:
        N /= 11
        eleven += 1
    result.append(eleven)

    print(f'#{t}', *result)