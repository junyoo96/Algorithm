# 11:43~ 12:00
# answer : 그룹 단어 개수 출력
# 그룹단어 : 한번 나온 문자가 끊겼다가 다시 나오지 않는 단어
#================================
n = int(input())

answer = 0
for _ in range(n):
    word = input()
    error = 0
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            new_word = word[i + 1:]

            if new_word.count(word[i]) > 0:
                error += 1
                break

    if error == 0:
        answer += 1

print(answer)