A = int(input())
nums = list(map(int, input().split()))
dp = [0] * A

dp[0] = nums[0]

for i in range(A):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])
        else:
            dp[i] = max(dp[i], nums[i])


print(max(dp))