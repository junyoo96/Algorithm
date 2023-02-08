# 5:25~5:27 / 5:27~5:32

# participant : 마라톤에 참여 선수 이름(1~100,000)
# completion : 완주 선수 이름(항상 participant보다 - 1)
# 참가자 이름(1~20 알파벳 소문자)
# 참가자 중에는 동명이인 있을 수 있음
# answer : 완주하지 못한 선수의 이름
#=====================================
# 최적화 코드 - hash값의 가감을 통한 풀이
def solution(participant, completion):
    answer = ''
    # 이름의 hash값의 가감을 통해 남은 hash값으로 완주하지 못한 선수의 이름을 알아내기 위해 사용
    tmp = 0
    # key: 이름의 hash값, value : 이름
    dic = {}
    for part in participant:
        # 이름의 hash값을 key로, 이름을 value로 저장
        dic[hash(part)] = part
        # 이름의 hash값을 더하기
        tmp += int(hash(part))
    for com in completion:
        # 완주한 선수 이름의 hash값을 빼기
        tmp -= hash(com)
    # 빼고 남은 hash값이 완주하지 못한 선수의 이름의 hash값이 됨
    answer = dic[tmp]

    return answer

#=====================================
# 내코드
from collections import defaultdict

def solution(participant, completion):
    # 완주하지 못한 선수 이름
    answer = ''

    check = defaultdict(lambda: 0)
    for c in completion:
        check[c] += 1

    for p in participant:
        if p in check:
            if check[p] > 0:
                check[p] -= 1
            else:
                answer = p
                break
        else:
            answer = p
            break

    return answer