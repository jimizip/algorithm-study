M, N = map(int, input().split())

def find_prime_list_under_number(M, N):
    prime_list = []
    for n in range(M, N + 1):
        if n < 2:
            continue
        if n == 2:
            prime_list.append(2)
            continue
        if n % 2 == 0:
            continue
        for i in range(3, int(n**0.5)+1):
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(M, N)
for i in result:
    print(i)