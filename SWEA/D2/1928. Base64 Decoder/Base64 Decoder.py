T = int(input())
for tc in range(1, T+1):
    s = input().strip()
    
    # Base64 색인표 (A-Z: 0-25, a-z: 26-51, 0-9: 52-61, +: 62, /: 63)
    table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    result = []
    
    # 4개씩 묶어서 처리 (4개 문자 = 24비트 -> 3바이트)
    for i in range(0, len(s), 4):
        # 4개 문자를 Base64 색인으로 변환 (각 6비트)
        a = table.index(s[i])      # 첫번째 6비트
        b = table.index(s[i+1])    # 두번째 6비트
        c = table.index(s[i+2]) if s[i+2] != '=' else 0  # 세번째 6비트
        d = table.index(s[i+3]) if s[i+3] != '=' else 0  # 네번째 6비트
        
        # 6비트 4개를 합쳐 24비트로 만든 후 8비트씩 분리
        # a를 18비트 왼쪽 시프트(<<): 6비트를 상위로 이동
        # b를 12비트 왼쪽 시프트: 두번째 6비트 배치
        # OR 연산(|)으로 비트 합침
        byte1 = (a << 2) | (b >> 4)  # 상위 8비트
        byte2 = ((b & 0xF) << 4) | (c >> 2)  # 중간 8비트, 0xF=15는 하위 4비트 마스크
        byte3 = ((c & 0x3) << 6) | d  # 하위 8비트, 0x3=3은 하위 2비트 마스크
        
        result.append(chr(byte1))
        if s[i+2] != '=':  # padding이 아니면 추가
            result.append(chr(byte2))
        if s[i+3] != '=':
            result.append(chr(byte3))
    
    print(f"#{tc} {''.join(result)}")
