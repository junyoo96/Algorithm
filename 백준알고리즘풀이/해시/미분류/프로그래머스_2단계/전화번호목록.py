# 5:40~6:10 / 6:10~6:15
# answer : 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 아니면 true
# phone_book(1~1,000,000)
# 전화번호(1~20)
# 같은 전화번호가 중복해서 들어있지는 않음

def solution(phone_book):
    answer = True

    count = {}
    for number in phone_book:
        count[number] = True

    for number in phone_book:
        for i in range(len(number) - 1): # 이중 for문 이지만 전화번호 길이 범위가 1~20이기 때문에 사실상 O(N)의 시간복잡도
            if number[:i + 1] in count:
                answer = False
                break

    return answer