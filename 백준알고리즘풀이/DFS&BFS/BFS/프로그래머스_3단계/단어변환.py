# 12:18~12:27/12:27~12:43
# 변환
# 한번에 한개의 알파벳만 변경 가능
# words에 있는 단어로만 변환 가능
# 모든 단어의 길이는 같음
# answer : begin에서 target으로 변환할때 변환 최소횟수
# 변환 할 수 없는 경우 0 반환
# ====================================
from collections import deque

def solution(begin, target, words):
    answer = 0

    length = len(begin)
    # 단어방문여부(dictionary)
    visited = {}
    # deque 생성 및 (begin 단어, 변환횟수) 추가
    queue = deque([(begin, 0)])
    # begin단어 방문처리
    visited[begin] = True

    # while queue:
    while queue:
        # 현재단어, 변환횟수 = deque에서 꺼내기
        current, count = queue.popleft()

        # 만약 현재단어가 target이라면
        if current == target:
            # answer = 변환횟수
            answer = count
            # break
            break

        # 각 단어 자릿수만큼 반복하면서
        for i in range(length):
            # 소문자 알파벳들을 반복하면서
            for j in range(ord('a'), ord('z') + 1):
                # 단어 변경
                changed = current[:i] + chr(j) + current[i + 1:]
                # 만약 변경한 단어를 방문한적이 없다면
                if changed not in visited and changed in words:
                    # queue에 (변경한 단어, 변환횟수 + 1)
                    queue.append((changed, count + 1))
                    # 변경한단어 방문처리
                    visited[changed] = True

    return answer