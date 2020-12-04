import sys
sys.stdin = open('토너먼트카드.txt')

def game(s, e):
    if s == e:
        return s
    # 절반씩 나누어서 게임 실행
    # 앞부분 승자, 뒷부분 승자 각각 구해서
    # 승자를 결정한다.
    center = (s+e) // 2
    v1 = game(s, center) # 앞단의 승자 인덱스
    v2 = game(center + 1, e) # 뒷단의 승자 인덱스

    # 두 그룹의 승자 중 이긴 사람을 반환
    # 1가위 2바위 3보
    v1_card = cards[v1]
    v2_card = cards[v2]
    if v1_card == 1: # 가위
        if v2_card == 2: #바위
            return v2
        else:
            return v1

    elif v1_card == 2: # 바위
        if v2_card == 3: # 보
            return v2
        else:
            return v1

    elif v1_card == 3: # 보
        if v2_card == 1: # 가위
            return v2
        else:
            return v1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    result = game(0, N-1)
    print("#{} {}".format(tc, result+1))


