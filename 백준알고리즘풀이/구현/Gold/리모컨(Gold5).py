# 최적화 코드
import sys

input = sys.stdin.readline
target = int(input())
num = int(input())
broken = list(input().split())
current = 100

answer = abs(current - target)

for channel in range(1000001):
    tmp = str(channel)
    for i in range(len(tmp)):
        if tmp[i] in broken:
            break
        else:
            if i == len(tmp) - 1:
                answer = min(answer, len(tmp) + abs(channel - target))

print(answer)

#============================================================================
# 내코드
# 9:58~10:41 / 10:41~ / 실패 - 아이디어는 맞았음

# 리모컨
# 0~9
# n : 이동하려는 채널
# answer : 어떤 버튼이 고장났는지 주어졌을 때, 채널 n으로 이동하기 위해 버튼을 최소 몇번 눌러야하는지 구하기
# 현재 채널 100번
# ==============================
import sys

input = sys.stdin.readline

answer = 0
# 목적지 리모컨 번호 입력
target = int(input())
# 고장난 버튼 개수 입력
num = int(input())
# 고장난 버튼 입력
broken_buttons = []
if num != 0:
    broken_buttons = list(input())
# 현재 채널
current = 100

# 만약 현재채널이 목적지 리모컨 번호라면
if target == current:
    # print(answer)
    print(answer)
# else
else:
    # 기호버튼 눌렀을 때 얼마나 눌러야 하는지 횟수 변수 = abs(목표채널 - 현재채널)
    answer = abs(target - current)

    isBroken = False
    # 채널을 50만번 반복하면서
    for i in range(1000001): # 주의 - 1000001
        isBroken = False
        # 현재 숫자를 리스트로 변환한 리스트를 반복하면서
        for j in list(str(i)):
            # 만약 현재 리스트의 숫자가 고장난 버튼에 포함된다면
            if j in broken_buttons:
                isBroken = True
                break

        if isBroken == False:
            # 눌러야되는 횟수 = 현재 숫자 길이 + abs(목표채널 - 현재 숫자)
            tmp = len(str(i)) + abs(target - i)
            # answer = min(answer, 눌러야되는 횟수)
            answer = min(answer, tmp)

    # answer 출력
    print(answer)