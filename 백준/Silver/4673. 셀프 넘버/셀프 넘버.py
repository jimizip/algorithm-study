def d(n):
    return n + sum(int(num) for num in str(n))

not_self_num = set()
for i in range(1, 10001):
    not_self_num.add(d(i))
    if i not in not_self_num:
        print(i)