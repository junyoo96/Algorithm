# 10:45~10:50/10:50~11:30

def solution(numbers, target):
    answer = 0

    def dfs(idx):

        if len(s) == len(numbers):
            if sum(s) == target:
                nonlocal answer
                answer += 1

            return

        for i in [-1, 1]:
            s.append(i * numbers[idx])
            dfs(idx + 1)
            s.pop()

    s = []
    dfs(0)

    return answer