# 9:32~9:58 / 10:13~10:50
# n : 송전탑 개수(2~100)
# wires : 전선 정보
# 2차원 배열(길이 n - 1)
# 송전탑
# 전선을 통해 하나의 트리 형태로 연결
# 전선들 중 하나를 끊어서 전력망 네트워크를 2개로 분할하려함
# 두 전력망이 갖게 되는 송전탑 개수를 최대한 비슷하게 맞추려함
# answer : 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값) 반환

def solution(n, wires):
    # dfs 함수(출발인덱스)
    def dfs(idx):
        # 방문처리
        visited[idx] = True

        # count 변수 = 0
        count = 1
        # 모든 송전탑 방문 여부(True)
        is_visited_all = True
        # 연결되어 있는 송전탑을 반복하면서
        for i in range(n):
            if new_wires[idx][i]:
                # 만약 해당 송전탑에 방문한적이 없다면
                if not visited[i]:
                    # count = dfs(송전탑)
                    count += dfs(i)
                    # 모든 송전탑 방문 여부 False
                    is_visited_all = False

        # 모든 송전탑 방문여부가 True라면
        if is_visited_all:
            return 1
        # 아니라면
        else:
            return count

    # 인접 행렬 형태로 wires 연결 저장하기
    new_wires = [[False] * n for _ in range(n)]

    for v1, v2 in wires:
        new_wires[v1 - 1][v2 - 1] = True
        new_wires[v2 - 1][v1 - 1] = True

    # 방문 여부
    visited = [False] * n

    # 송전탑 개수의 최소 차이
    answer = 1e9
    # wires를 반복하면서
    for v1, v2 in wires:
        # 방문 초기화
        visited = [False] * n

        # 연결 일시적으로 끊기
        new_wires[v1 - 1][v2 - 1] = False
        new_wires[v2 - 1][v1 - 1] = False
        # 송전탑개수1 += dfs(첫번재 송전탑에서 출발 - 1)
        first = dfs(v1 - 1)
        # 송전탑개수2 += dfs(두번째 송전탑에서 출발 - 1)
        second = dfs(v2 - 1)
        # 끊긴 거 다시 연결
        new_wires[v1 - 1][v2 - 1] = True
        new_wires[v2 - 1][v1 - 1] = True

        # 차이계산 해서 최소값 구하기
        answer = min(answer, abs(first - second))

    return answer