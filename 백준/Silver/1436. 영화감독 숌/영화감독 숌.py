N = int(input())
num = 666
cnt = 0

while True:
    if '666' in str(num):
        cnt += 1
    if N == cnt:
        break
    num += 1

print(num)