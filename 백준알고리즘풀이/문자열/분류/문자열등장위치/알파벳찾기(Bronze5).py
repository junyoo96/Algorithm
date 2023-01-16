# answer : a~z까지의 각각의 알파벳에 대해 처음 등장하는 위치 공백으로 구분해 출력

word = input()
locations = [-1] * 26
for i in range(len(word)):
    if locations[ord(word[i]) - ord('a')] == -1:
        locations[ord(word[i]) - ord('a')] = i
print(*locations)