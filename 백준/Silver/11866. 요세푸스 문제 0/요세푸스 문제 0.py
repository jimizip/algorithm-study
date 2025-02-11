N, K = map(int, input().split())
people = list(range(1, N+1))
result = []
i = 0

while people:
    i = (i + K-1) % len(people)
    result.append(people.pop(i))

print("<" + ", ".join(map(str, result)) + ">")