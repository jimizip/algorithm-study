import sys
input = sys.stdin.readline
S = input().strip()
stack = []  # 스택
result = ''
tag = False

for char in S:
    # 태그 시작
    if char == '<':
        # 스택에 쌓인 단어 처리
        while stack:
            result += stack.pop()
        tag = True
        result += char # '<' 추가가
    
    # 태그 종료
    elif char == '>':
        tag = False
        result += char
    
    # 태그 내부 문자
    elif tag:
        result += char
    
    # 공백 처리 (단어 구분분)
    elif char == ' ':
        while stack:
            result += stack.pop()
        result += char
    
    # 일반 문자
    else:
        stack.append(char)

# 남은 문자 처리
while stack:
    result += stack.pop()

print(result)