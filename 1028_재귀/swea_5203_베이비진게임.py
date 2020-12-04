import sys
sys.stdin = open('swea_5203_베이비진게임.txt')


def check_winner(check, player):
    cnt = 0
    for j in range(len(check)):
        # run 확인
        if check[j] != 0:
            cnt += 1
            if cnt >= 3:
                return player # player가 승리 했다.
        else:
            cnt = 0

        # triplet 확인
        if check[j] >= 3:
            return player

    return 0 # 승부가 나지 않았다.


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    # print(cards)

    p1_check = [0] * 10
    p2_check = [0] * 10
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            p1_check[cards[i]] += 1
            if sum(p1_check) >= 3:
                winner = check_winner(p1_check, 1)
                if winner:
                    break

        else:
            p2_check[cards[i]] += 1
            if sum(p2_check) >= 3:
                winner = check_winner(p2_check, 2)
                if winner:
                    break

    print('#{} {}'.format(tc, winner))
