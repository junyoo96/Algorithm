# 폭발문자열
    # 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐짐
    # 같은 문자를 2개 이상 포함하지 않음
# 폭발과정
    # 만약 문자열이 폭발 문자열을 포함하고 있는 경우, 모든 폭발 문자열이 폭발
        # 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만듬
        # 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수 있음
    # 폭발은 폭발 문자열 문자열에 없을 때까지 반복

# answer : 모든 폭발이 끝난 후 남은 문자열 출력
    # 남아있는 문자가 없는 경우, FRULA 출력
#===============================================================
# 최적화 코드
import sys

input = sys.stdin.readline

answer = ""
# 문자열 입력(1~1,000,000)
string = input().rstrip() # 주의 - rstrip(readline() 입력받을시 맨끝에 저장되는 개행문자 \n을 제거하기위해 사용)
# 폭발 문자열 입력(1~36)
bomb_string = input().rstrip()
bomb_string_len = len(bomb_string)

# 중요 - 시간 제한 때문에 stack으로 문자열 폭발 구현 - O(N) 소요
stack = []
for char in string: # O(N)
    stack.append(char)
    # 만약 넣은 문자열중 최근 문자열들이 폭탄 문자열과 같다면
    if ''.join(stack[-bomb_string_len:]) == bomb_string: # 중요 - 맨 뒤부터 리스트 값 가져오는 방법
        for _ in range(bomb_string_len): # O(1) - 상수시간
            stack.pop()

if stack:
    answer = ''.join(stack)
else: # 문자열이 남아있지 않다면
    answer = "FRULA"

print(answer)

#===============================================================
# 내 코드
# 10:11~10:40 / 10:50~ / 시간초과로 실패

# 문자열 입력(1~1,000,000)
string = input()
# 폭발 문자열 입력(1~36)
bomb = input()

# answer = ""
answer = ""
# while True
while True:
    # split된 문자열 = 폭발 문자열 기준으로 split
    split_strings = string.split(bomb)

    # 만약 split된 문자열이 1이라면
    if len(split_strings) == 1:
        split_string = "".join(split_strings)

        # 만약 폭발 문자열과 같다면
        if split_string == "":
            # answer = FRULA
            answer = "FRULA"
        # else
        else:
            # answer = split된 문자열
            answer = split_string

        # break
        break

    # split된 문자열을 반복하면서
    string = ""
    for split_string in split_strings:
        # split된 문자열을 다시 합치기
        string += split_string

# answer 출력
print(answer)