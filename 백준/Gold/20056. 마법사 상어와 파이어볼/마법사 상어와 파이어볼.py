N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # 자신의 방향으로 속력으로 이동
    for i in range(len(arr)):
        arr[i][0] = (arr[i][0] + di[arr[i][4]] * arr[i][3]) % N + 1
        arr[i][1] = (arr[i][1] + dj[arr[i][4]] * arr[i][3]) % N + 1

    # 정렬(행과 열 기준으로 -> 같은 칸에 있는 것 찾기 용)
    arr.sort(key=lambda x: (x[0], x[1]))

    # padding 넣기(맨 마지막 배열까지 에러나지 않고 볼 수 있게 하기 용)
    arr.append([100, 100, 0, 0, 0])

    # 새롭게 나눠진거 or 혼자 방향만 바꾼거 넣기 용
    new_arr = []

    i = 0
    while i < len(arr) - 1:
        ri, cj, m, s, d = arr[i]
        flag = 0
        for j in range(i+1, len(arr)):
            if (ri, cj) == (arr[j][0], arr[j][1]):
                m += arr[j][2]
                s += arr[j][3]
                if d % 2 != arr[j][4] % 2:
                    flag = 1
            else:
                # 같은게 없어서 한 개만 추가 하면 된다?
                if j - i == 1:
                    new_arr.append(arr[i])
                else:
                    new_m = m // 5
                    # m이 0이면 소멸!!
                    if new_m > 0:
                        for dir in range(flag, 8, 2):
                            new_arr.append([ri, cj, new_m, (s // (j - i)), dir])
                break
        # j까지 합쳤으니까 i 바꿔주기
        i = j
    # 이동한 새로운 arr로 바꿔주기
    arr = new_arr

result = 0
for mm in arr:
    result += mm[2]

print(result)