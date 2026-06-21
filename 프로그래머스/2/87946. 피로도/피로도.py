def DFS(answer, count, k, visited, dungeons):
    answer = max(answer, count)

    for i in range(len(dungeons)): 
        #최소 필요 피로도가 더 크거나 이미 방문한 던전이면
        if k < dungeons[i][0] or visited[i]:
            continue

        visited[i] = True 
        
        # 던전 방문수 + 1, 내 피로도 - 현재 던전 소모 필요도, 방문 처리 배열,던전 배열
        answer = DFS(answer, count+1, k-dungeons[i][1], visited, dungeons)

        visited[i] = False
        
    return answer

def solution(k, dungeons):
    answer = 0
    
    visited = [False] * len(dungeons) 
    count = 0

    answer = DFS(answer, count, k, visited, dungeons)
    
    return answer