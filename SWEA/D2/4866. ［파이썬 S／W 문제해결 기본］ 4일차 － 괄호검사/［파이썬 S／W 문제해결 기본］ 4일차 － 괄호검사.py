T = int(input())
for tc in range(1, T + 1):
    code = input()

    stack = []  # 스택 초기화
    result = 1  # 정상이면 1, 아니면 0

    # 괄호 매칭 딕셔너리 (닫는 괄호 -> 여는 괄호)
    matching = {')': '(', '}': '{'}

    for char in code:
        # 여는 괄호이면 스택에 push
        if char in '({':
            stack.append(char)

        # 닫는 괄호이면 검사
        elif char in ')}':
            # 스택이 비어있으면 짝이 안 맞음
            if not stack:
                result = 0
                break

            # 스택 top과 매칭되는지 확인
            top = stack.pop()  # pop(): 마지막 요소를 제거하고 반환
            if matching[char] != top:  # 짝이 안 맞으면
                result = 0
                break

    # 스택에 여는 괄호가 남아있으면 짝이 안 맞음
    if stack:
        result = 0

    print(f"#{tc} {result}")
