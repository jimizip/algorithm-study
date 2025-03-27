N = list(input())

N.sort(reverse=True)

result = ''

for i in N:
    result += i

print(result)