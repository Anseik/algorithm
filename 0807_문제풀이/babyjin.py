# baby-gin
# 원소수가 3개인 부분집합을 생성
# 1이 3개인 6자리 2진수 --> 0도 3개

cards = [5, 4, 1, 2, 3, 6]

for subset in range(1 << 6):
    # 각자리 값을 확인

    A, B = [], []
    for i in range(6):
        if subset & (1 << i):
            A.append(cards[i])
        else:
            B.append(cards[i])

    if len(A) == len(B):
        print(A, B)

