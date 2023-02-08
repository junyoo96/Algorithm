# 1:21~1:41/1:41~2:00

# 피로도(0이상 정수)
# 최소 필요 피로도
# 가지고 있어야 하는 최소한 피로도
# 소모 피로도
# 던전 탐험 후 소모되는 피로도
# k : 유저의 현재 피로도(1~5,000)
# dungenons : 던전별 [최소 필요 피로도(1~1000), 소모 피로도(1~1000)](1~8)
# 최소 필요 피로도 >= 소모 피로도
# answer : 유저가 탐험할 수 있는 최대 던전수
#=================================
# dfs로 permuations 직접 구현
def solution(k, dungeons):
    def dfs():

        if len(s) == length:
            current_hp = k
            count = 0
            for require_hp, lose_hp in s:
                if current_hp >= require_hp:
                    current_hp -= lose_hp
                    count += 1

            nonlocal answer # 주의 - 외부 함수의 변수 접근할 때 현재 함수의 로컨 변수가 아니라는 것을 명시해주어야함
            answer = max(answer, count)

        for i in range(length):
            if not visited[i]:
                s.append(dungeons[i])
                visited[i] = True
                dfs()
                s.pop()
                visited[i] = False

    answer = 0
    length = len(dungeons)
    s = []
    visited = [False] * length
    dfs()

    return answer

#=====================================
# permutations 사용
from itertools import permutations
def solution(k, dungeons):
    answer = 0

    for dungeon in permutations(dungeons, len(dungeons)):
        current_hp = k
        count = 0
        for require_hp, lose_hp in dungeon:
            if current_hp >= require_hp:
                current_hp -= lose_hp
                count += 1

        answer = max(answer, count)

    return answer

if __name__ == '__main__':
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k, dungeons))