# 9:20~
from collections import deque

# 균형잡힌 괄호 문자열의 인덱스 반환
def get_balanced_index(text):
    cnt = 0 #왼쪽 괄호의 개수
    for idx, c in enumerate(text):
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return idx

# 올바른 괄호 문자열 인지 판단
def check_proper_text(text):
    cnt = 0
    for i in text:
        if i == '(':
            cnt += 1
        else:
            # 쌍이 맞지 않는데 ')' 괄호가 나온 경우
            if cnt == 0:
                return False
            cnt -= 1
    # 쌍이 맞는 경우에 True 반환
    return True

def solution(p):
    answer = ''

    # 입력이 빈 문자일인 경우
    if p == '':
        return answer
    # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    idx = get_balanced_index(p)
    u = p[:idx + 1]
    v = p[idx + 1:]

    # 문자열 u가 '올바른 괄호 문자열' 인경우
    if check_proper_text(u):
        answer = u + solution(v)
    # 문자열 u가 '올바른 괄호 문자열' 아닌경우
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        # string은 직접 index지정해서 변경하는 것이 안되기 때문에 list로 변경
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer