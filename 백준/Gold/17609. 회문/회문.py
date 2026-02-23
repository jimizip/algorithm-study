def is_palindrome(word, s, l):
    while s < l :
        if word[s] != word[l]:
            return False, s, l
        s += 1
        l -= 1
    return True, s, l

T = int(input())
for _ in range(T):
    word = input()
    result, s, l = is_palindrome(word, 0, len(word)-1)
    if result:
        print(0)
    else:
        result, _, _= is_palindrome(word, s+1, l)
        if result:
            print(1)
        else:
            result, _, _ = is_palindrome(word, s, l-1)
            if result:
                print(1)
            else:
                print(2)