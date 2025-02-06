N = int(input())
slist = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    # print(f"\n--- i = {i} ---")
    # print(f"상담 기간: {slist[i][0]}일, 금액: {slist[i][1]}원")
    # 조건 분기 전 dp 상태
    # print(f"현재 dp[{i}~{N}]: {dp[i:]}")
    if i + slist[i][0] > N:
        # print(f"❌ 상담 불가 (i + 기간 = {i + slist[i][0]} > {N}) → dp[{i}] = dp[{i+1}] ({dp[i+1]}원)")
        dp[i] = dp[i+1]
    else:
        # print(f"⭕ 상담 가능 (i + 기간 = {i + slist[i][0]} ≤ {N})")
        # print(f"   선택1: 상담 안함 → dp[{i+1}] ({dp[i+1]}원)")
        # print(f"   선택2: 상담 함 → {slist[i][1]}원 + dp[{i + slist[i][0]}] ({dp[i + slist[i][0]]}원)")
        dp[i] = max(dp[i+1], slist[i][1] + dp[i+slist[i][0]])

# print("\n최종 dp 배열:", dp)
print(dp[0])