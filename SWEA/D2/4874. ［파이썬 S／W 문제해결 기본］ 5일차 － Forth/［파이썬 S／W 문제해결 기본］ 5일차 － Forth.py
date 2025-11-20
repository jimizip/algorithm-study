T = int(input())
for tc in range(1, T + 1):
    tokens = input().split() 
    stack = []
    result = 0
    error = False

    for token in tokens:
        if token == '.': 
            if len(stack) == 1:
                result = stack.pop()
            else:
                error = True
            break

        elif token in '+-*/': 
            if len(stack) < 2:
                error = True
                break

            b = stack.pop()  # 두 번째 피연산자
            a = stack.pop()  # 첫 번째 피연산자

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)  # 정수 나눗셈

        else: 
            stack.append(int(token))

    if error:
        print(f"#{tc} error")
    else:
        print(f"#{tc} {result}")