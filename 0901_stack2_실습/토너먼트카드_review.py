import sys
sys.stdin = open('토너먼트카드.txt')


def rps(s, e):
    if s == e:
        return s
    center = (s + e) // 2
    g1 = rps(s, center) # 앞단 승자의 인덱스
    g2 = rps(center + 1, e) # 뒷단 승자의 인덱스

    c1 = cards[g1]
    c2 = cards[g2]

    # 1: 가위, 2: 바위, 3: 보
    if c1 == 1:
        if c2 == 2:
            return g2
        else:
            return g1
    if c1 == 2:
        if c2 == 3:
            return g2
        else:
            return g1
    if c1 == 3:
        if c2 == 1:
            return g2
        else:
            return g1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    # print(N)
    # print(cards)

    result = rps(0, N - 1)
    victory = result + 1
    print("#{} {}".format(tc, victory))