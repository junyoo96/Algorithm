# 11:33~ 아이디어 생각 못함
# 일관성
    # 한 번호가 다른 번호의 접두어인 경우가 없어야함
# n : 전화번호 수(1~10000)
# 전화번호(1~10)
# 같은 전화번호는 없음
# answer : 전화번호 목록이 일관성이 인지 아닌지 출력
# =======================
import sys
input = sys.stdin.readline

# t 입력
t = int(input().rstrip())
# t 만큼 반복하면서
for _ in range(t):
    # n 입력
    n = int(input().rstrip())
    # n만큼 전화번호 목록 입력
    numbers = [input().rstrip() for _ in range(n)]
    # 중요 - 전화번호 목록 오름차순 정렬하면 pefix의 가능성이 있는 번호가 앞뒤로 정렬되므로 바로 뒤에 있는 번호만 확인하면 됨
    numbers.sort()

    flag = True

    answer = "YES"
    for i in range(n - 1):
        length = len(numbers[i])
        # 바로 뒤에 있는 번호만 확인
        if numbers[i] == numbers[i + 1][:length]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")