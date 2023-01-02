# 1:42~

# 부서장 : 루트
# 부서장과 각 직원은 왼쪽과 오른쪽 직원 갖음
# 말단 직원 : 부하직원이 없는 직원

# H : 조직도 트리 높이
# R : 업무 진행일

# 처음에는 말단 직원들만 각각 K개의 순서가 정해진 업무를 갖음
# 각 날짜에 남은 업무가 있는 경우, 말단 직원은 하나의 업무를 처리해 상사에게 올림
# 다른 직원들도 대기하는 업무가 있는 경우, 업무를 올라온 순서대로 하나씩 처리해 상사에 올림
# 단, 홀수번째 날짜에는 왼쪽 부하직원이 올린 업무
# 짝수번째 날짜에는 오른쪽 부하직원이 올린 업무 처리

# 부서장이 처리한 일은 완료된 것
# 업무를 올리는 것은 모두 동시 진행

# answer : 처리가 완료된 업무들의 번호의 합을 출력
# ====================================================
import sys
import math
from collections import deque

# answer 변수
answer = 0
# 높이 H, 말단 업무개수 K, 업무 진행날짜수 R 입력
h, k, r = map(int, input().split())

# 1. 트리 설계
# 모든 직원 수 계산
workers_num = int(math.pow(2, h + 1)) - 1
print("모든 직원수", workers_num)
# 말단 직원 수 계산
tail_workers_num = int(math.pow(2, h))
print("말단 직원 수", tail_workers_num)

# 말단직원들에 대한 queue 생성
tail_workers_queue = []
for i in range(tail_workers_num):
    works = list(map(int, input().split()))
    tail_workers_queue.append(deque(works))

# 말단 이외의 직원들에 대한 queue 생성
workers_queue = [[deque(), deque()] for _ in range(tail_workers_num + 1)]

# 루트노드의 index/2가 부모 노드의 index

print(workers_queue)
print(tail_workers_queue)

# 2. R일만큼 업무 진행
# R만큼 반복하면서
for i in range(1, r + 1):
    # is_odd - 날짜가 홀수인지 짝수인지 체크
    is_odd = 0 if i % 2 == 0 else 1

    # 부서장 업무 처리
    # queue[1][check]에서 업무 꺼내서 answer에 더하기
    if workers_queue[1][is_odd]:
        print("부서장 업무 처리")
        answer += workers_queue[1][is_odd].popleft()

    # 중간급 직원들 업무 처리
    # 높은 순부터 차례대로 queue[index][check]에 대해 업무를 하나 꺼내기
    # index/2인 부모노드에 왼쪽, 오른쪽 직원을 고려해 추가
    for j in range(2, workers_num - tail_workers_num + 1): # 여기 모르겠음
        print("번째", j)
        work = workers_queue[j][is_odd].popleft()
        # 부모idx
        parent_idx = j // 2
        # 짝수 index인 경우
        if j % 2 == 0:
            workers_queue[parent_idx][0].append(work)
        else:
            workers_queue[parent_idx][1].append(work)

    # 말단급 직원들 업무 처리
    # 처리해야하는 업무가 남아있을 경우, queue_tail[index]에서 업무 하나 꺼내 부모 노드에 추가
    for j in range(tail_workers_num + 2, workers_num + 1):
        work = tail_workers_queue[j][is_odd].popleft()
        # 부모idx
        parent_idx = j // 2
        # 짝수 index인 경우
        if j % 2 == 0:
            workers_queue[parent_idx][0].append(work)
        else:
            workers_queue[parent_idx][1].append(work)

    print(workers_queue)
    print(tail_workers_queue)
    print("==========================")

print(answer)





