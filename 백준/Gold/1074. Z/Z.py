N, r, c = map(int, input().split())

result = 0

while N != 0:
    N -= 1
    half = 2 ** N

    if r < half and c < half:
        result += half * half * 0
    elif r < half and c >= half:
        result += half * half * 1
        c -= half
    elif r >= half and c < half:
        result += half * half * 2
        r -= half
    else:
        result += half * half * 3
        r -= half
        c -= half

print(result)