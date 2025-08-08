T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# A 배열의 모든 부 배열의 합을 리스트에 저장
sums_A = []
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += A[j]
        sums_A.append(current_sum)

# B 배열의 모든 부 배열의 합을 딕셔너리에 {합: 개수} 형태로 저장
sums_B_counts = {}
for i in range(m):
    current_sum = 0
    for j in range(i, m):
        current_sum += B[j]
        sums_B_counts[current_sum] = sums_B_counts.get(current_sum, 0) + 1

answer = 0
for sum_a in sums_A:
    # B의 합은 T - sum_a
    target_b = T - sum_a
    
    # 딕셔너리에서 target_b의 개수를 찾아 더함
    answer += sums_B_counts.get(target_b, 0)

print(answer)