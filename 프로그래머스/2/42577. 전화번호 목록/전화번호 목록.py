def solution(phone_book):
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1
    
    for i in phone_book:
        tmp = ""
        for j in i:
            tmp += j
            if tmp in hash_map and tmp != i:
                return False
    
    return True