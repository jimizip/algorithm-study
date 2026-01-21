string = input()
arr = [-1] * 26

for i in range(len(string)):
    tmp_index = ord(string[i]) - ord('a')
    if arr[tmp_index] == -1:
        arr[tmp_index] = i

print(*arr)