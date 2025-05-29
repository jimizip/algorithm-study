num_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
put = list(input())
time = 0
for i in put:
    for j in num_list:
        if i in j:
            time += num_list.index(j)+3
print(time)