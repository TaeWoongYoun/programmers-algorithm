from collections import deque

def solution(n, computers):
    visited = [False] * n
    networks = 0
    
    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            
            while queue:
                current = queue.popleft()
                for j in range(n):
                    if computers[current][j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True
            networks += 1
            
    return networks