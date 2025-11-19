T = int(input())
for tc in range(1, T+1):
    n, hex_num = input().split()
    
    result = ""
    
    # 16진수 각 자릿수를 2진수 4자리로 변환
    for h in hex_num:
        # int(h, 16): 16진수 문자를 10진수로 변환
        decimal = int(h, 16)
        
        # bin(): 10진수를 2진수 문자열로 변환 ('0b'로 시작)
        # [2:]: '0b' 제거
        binary = bin(decimal)[2:]
        
        # zfill(4): 4자리가 되도록 앞에 0 채움
        # 예: '11' -> '0011'
        result += binary.zfill(4)
    
    print(f"#{tc} {result}")
