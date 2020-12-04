import sys
sys.stdin = open('swea_5203_베이비진게임_solution.txt')

def check(arr): # arr에 run이나 triplet이 있으면 True, 없으면 False
    # run 검사
    # triplet인지 검사
    for i in range(len(arr)):
        if i < len(arr) - 2 and arr[i] > 0:
            if arr[i + 1] > 0 and arr[i + 2] > 0:
                return True
        if arr[i] == 3:
            return True

    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    # print(cards)
    # 각 플레이어가 어떤 카드를 몇 장 받았는지 저장하는 배열
    p1 = [0] * 10
    p2 = [0] * 10
    for i in range(len(cards)):
        if i % 2 == 0:
            p1[cards[i]] += 1
        else:
            p2[cards[i]] += 1
        # 카드를 받을 때마다, run이나 triplet이 있는지 검사
        if check(p1):
            print('#{} 1'.format(tc))
            break
        if check(p2):
            print('#{} 2'.format(tc))
            break
    else:
        print('#{} 0'.format(tc))