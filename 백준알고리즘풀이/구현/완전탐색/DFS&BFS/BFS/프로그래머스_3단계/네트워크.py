# 11:57~12:00/12:00~12:07
# answer : 네트워크의 개수
#================================
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True

            while queue:
                current = queue.popleft()

                for idx, value in enumerate(computers[current]):
                    if value == 1 and idx != current and not visited[idx]:
                        queue.append(idx)
                        visited[idx] = True

            answer += 1

    return answer