# 9:10~
from collections import deque

t = int(input())
for _ in range(t):
    commands = input()
    n = int(input())
    nums = deque(input()[1:-1].split(',')) # 주의 - 첫번째와 마지막 문자 제거하는 방법
    if n == 0:
        nums = []

    # 중요 - 뒤집기 명령이 나올 때마다 몇번 뒤집어졌는지 카운트해 flag에 저장
    # flag없이 뒤집기 명령이 나올 때마다 뒤집으면 시간초과
    flag = 0

    for command in commands:
        if command == "R":
            flag += 1
        else:
            if len(nums) == 0:
                print("error")
                break
            if flag % 2 == 0:
                # 정방향이니까 원래대로 앞쪽에서 빼기
                nums.popleft()
            else:
                # 뒤집혀 있는 상태니까 뒤쪽에서 빼기
                nums.pop()

    else:
        # 뒤집기 상태라면 뒤집기
        if flag % 2 != 0:
            nums.reverse()

        print("[" + ','.join(nums) + "]")