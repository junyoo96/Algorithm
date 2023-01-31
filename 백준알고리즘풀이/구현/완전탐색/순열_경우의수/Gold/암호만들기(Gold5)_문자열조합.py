# 10:26~10:29/10:29~10:52

# L : 암호를 구성하는 알파벳 개수
# 최소 한개 모음과 최소 두개의 자음으로 구성
# 알파벳이 암호에서 증가하는 순서로 배열됨(조합)
# C : 문자 종류 개수
# ===============================
def dfs(idx):
    if len(s) == l:
        ja = 0
        mo = 0
        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u']:
                mo += 1
            else:
                ja += 1

        if ja >= 2 and mo >= 1:
            print(''.join(s))

    for i in range(idx, c):
        s.append(alphabets[i])
        dfs(i + 1)
        s.pop()

l, c = map(int, input().split())
alphabets = input().split()
alphabets.sort()
s = []

dfs(0)