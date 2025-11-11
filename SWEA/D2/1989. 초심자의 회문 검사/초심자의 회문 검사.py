T = int(input())
for t in range(1, T+1):
    word = input()
    reverse_word = ''
    for i in range(len(word)-1, -1, -1):
        reverse_word += word[i]

    if word == reverse_word:
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')