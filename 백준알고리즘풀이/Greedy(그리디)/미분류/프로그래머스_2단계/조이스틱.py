# 참고 : https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
def solution(name):
    # 조이스틱 조작 횟수
    answer = 0

    # 기본적인 최소 좌우이동 횟수는 길이 - 1(예를 들어 AAA일 경우)
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 1. 상,하 방향의 관점
        # "A부터 오름차순으로 현재 알파벳까지 바꾸기 위한 횟수"와 "Z부터 오름차순으로 현재 알파벳까지 바꾸기 위한 횟수" 비교
        # Z에서 1을 더하는 이유는 모든 알파벳은 A부터 시작하기 때문에 Z로 먼저 바꾸기 위해 횟수 1번이 필요하기 때문
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 중요 - 2. 좌,우 방향의 관점
        # 해당 알파벳 다음부터 연속된 A 문자열이 끝나고 다른 알파벳이 시작되는 지점 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 다음 3가지를 비교해서 최소 이동횟수 선택
            # 일반방식 : "왼쪽에서 오른쪽으로만 이동하는 일반적인 경우의 움직이는 횟수"
            # 연속된 A의 왼쪽 시작방식 : "연속된 A의 왼쪽(A시작 직전 알파벳)으로 커서를 먼저 이동하고, 방향을 바꾸어 하나씩 알파벳을 변경하면서 연속된 A의 오른쪽(A끝 직후 알파벳)으로 이동하기(첫번째 알파벳에서 왼쪽으로 이동하면 마지막 알파벳으로 이동할 수 있으므로)"
                # i + i + len(name) - next
                    # 첫번재 i : 연속된 A의 왼쪽으로(첫번째 알파벳부터 A가 나오기전까지 왼쪽에서 오른쪽으로) 이동하는 횟수
                    # 두번째 i : A를 마주치면 첫번재 알파벳까지 온방향으로 되돌아갈때 이동하는 횟수
                    # len(name) - next : 문자열의 끝으로 이동해서 왼쪽 방향으로 A가 나오기전까지 이동횟수
            # 연속된 A의 오른쪽 시작방식 : "연속된 A의 오른쪽(A끝 직후 알파벳)으로 커서를 먼저 이동하고, 방향을 바꾸어 하나씩 알파벳을 변경하면서 연속된 A의 왼쪽(A시작 직전 알파벳)으로 이동하기(마지막 알파벳에서 오른쪽으로 이동하면 첫번째 알파벳으로 이동할 수 있으므로)"
                    # (len(name) - next) + (len(name - next)) + i
                        # len(name) - next : 연속된 A의 오른쪽으로 커서를 이동하는 횟수
                        # len(name) - next : 다시 연속된 A의 오른쪽에서 왼쪽방향으로 알파벳의 끝까지 이동하는 횟수
                        # i : 첫번째 알파벳부터 연속된 A의 왼쪽으로 이동하는 횟수
        min_move = min(min_move, i + i + len(name) - next, (len(name) - next) + (len(name) - next) + i)

    # 알파벳 상하이동 최소 횟수에 최소 좌우이동 횟수 더하기
    answer += min_move
    return answer

if __name__ == '__main__':
    print(solution("JEROEN"))