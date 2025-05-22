for tc in range(1, 11):
    N, num_str = input().split()
    stack = []
    
    for i in num_str:
        # 스택이 비어있거나, 현재 문자가 스택의 마지막막과 다르면 push
        if not stack or stack[-1] != i:
            stack.append(i)
        # 스택의 top과 현재 문자가 같으면 (중복 쌍) pop
        else:
            stack.pop()
    
    print(f'#{tc} {"".join(stack)}')