data = input()
for i in range(0, len(data), 10):
    # 슬라이싱할 때 index를 초과해도 알아서 list 길이에 맞게 처리해줌
    print(data[i:i + 10])