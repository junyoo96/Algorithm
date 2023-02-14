# 10:32~10:55/10:55~

# 최적화 코드
from collections import defaultdict
def solution(tickets):
    answer = []

    # {시작점: [도착점리스트]} 형태로 그래프 생성
    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)

    # 중요 - 도착점 리스트를 역순 정렬
        # 알파벳 순서상 빠른 것이 우선시 되므로, pop할 때 맨끝에서 가장 알파벳이 먼저인 공항을 가져오기 위함
        # 이를 통해 모든 경로를 탐색하지 않아도됨
    for airport in graph.keys():
        graph[airport].sort(reverse=True)

    # 중요 - stack사용, 출발지는 항상 ICN이므로 stack에 먼저 넣어두기
    stack = ["ICN"]
    # DFS로 모든 노드 순회
    while stack:
        # 스택에서 가장 위의 저장된 데이터 꺼내오기
        top = stack.pop()

        # top이 그래프에 없거나(현재공항에서 출발하는 항공권이 없거나), top을 시작점으로 하는 티켓이 없는 경우(현재공항에서 출발하는 항공권이 남아있지 않은 경우)path에 저장
        if top not in graph or not graph[top]:
            # 더이상 현재 공항(노드)에서 이동할 수 없으므로 경로의 마지막이라는 의미가 됨
            # 따라서, answer(경로)에 현재 공항 추가
            answer.append(top)
        # top을 다시 스택에 넣고 top의 도착점 중 가장 마지막 지점을 꺼내와 스택에 저장
        else:
            # 현재공항 다음에 다음공항이 오도록 먼저 현재공항을 stack에 추가
            stack.append(top)
            # 현재 공항에서 갈 수 있는 공항을 꺼내서 스택에 저장(알파벳 역순으로 공항을 정렬했기 때문에 pop()한 공항이 알파벳이 가장 앞서는 공항인 것을 보장)
            stack.append(graph[top].pop())

    # path를 뒤집어서 반환(stack에 들어갈때 역순으로 들어감으로)
    return answer[::-1]

if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
