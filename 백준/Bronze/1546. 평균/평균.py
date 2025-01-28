N = int(input())

score = list(map(int, input().split()))

score.sort(reverse=True)

result = []
tmp = 0
for i in score:
    tmp = i/score[0]*100
    result.append(tmp)

print(sum(result)/N)