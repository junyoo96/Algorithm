# 12:27~12:38 // 처음에 문제 의미 이해못했음, 알고나서는 쉽게 풀음

# - 기준으로 분리
data = input().split("-")

answer = 0
# - 기준으로 분리된 요소들을 반복하면서
for i in range(len(data)):
    # 분리된 요소의 합 저장
    tmp = 0
    # 분리된 요소에서 +가 포함된 부분에 대한 계산
    elements = data[i].split("+")
    # 각 분리 요소의 합 계산
    for e in elements:
        tmp += int(e)

    # 처음 부분은 항상 양수이므로 더하기
    if i == 0:
        answer += tmp
    # 이후부터는 -로 분리된 부분이므로 빼기
    else:
        answer -= tmp

print(answer)