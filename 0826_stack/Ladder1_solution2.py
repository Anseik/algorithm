import sys
sys.stdin = open('Ladder1.txt')

# 지나온 길을 지우기
# 방문표시 하기
# 진행 중인 방향 정보
# 위로 가는 중 : 오른쪽, 왼쪽, 위
# 왼쪽으로 가는 중 : 왼쪽, 위
# 오른쪽으로 가는 중 : 오른쪽, 위

def check(x, y):
    if x < 0 or x >= 100 or y < 0 or y >= 100: return False
    if arr[x][y] == 0: return False
    return True


def ladder(x, y):
    if x == 0:
        global ans; ans = y
        return
    else:
        arr[x][y] = 0
        # 왼쪽으로 가는 경우(현재 진행방향이 위 또는 왼쪽, 즉 현재 진행방향이 오른쪽이 아닐때)
        if check(x, y - 1):
            ladder(x, y -1)
        # 오른쪽으로 가는 경우(현재 진행방향이 위 또는 오른쪽, 즉 현재 진행방향이 왼쪽이 아닐때)
        elif check(x, y + 1):
            ladder(x, y + 1)
        # 그외(위로 가는 경우)
        else:
            ladder(x - 1, y)


def ladder2(x, y):
    if x == 0:
        return y
    else:
        arr[x][y] = 0
        # 왼쪽으로 가는 경우(현재 진행방향이 위 또는 왼쪽, 즉 현재 진행방향이 오른쪽이 아닐때)
        if check(x, y - 1):
            return ladder2(x, y -1)
        # 오른쪽으로 가는 경우(현재 진행방향이 위 또는 오른쪽, 즉 현재 진행방향이 왼쪽이 아닐때)
        elif check(x, y + 1):
            return ladder2(x, y + 1)
        # 그외(위로 가는 경우)
        else:
            return ladder2(x - 1, y)

for tc in range(1, 11):
    case_num = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착점을 찾는다.
    x = y = 0
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break

    # # 방법
    # dir = 0 # 방향 정보 저장 0: 위, 1: 좌, 2: 우
    #
    # while x:
    #     # 왼쪽으로 가는 경우(현재 진행방향이 위 또는 왼쪽, 즉 현재 진행방향이 오른쪽이 아닐때)
    #     if dir != 2 and check(x, y - 1):
    #         y -= 1; dir = 1
    #     # 오른쪽으로 가는 경우(현재 진행방향이 위 또는 오른쪽, 즉 현재 진행방향이 왼쪽이 아닐때)
    #     elif dir != 1 and check(x, y + 1):
    #         y += 1; dir = 2
    #     # 그외(위로 가는 경우)
    #     else:
    #         x -= 1; dir = 0
    # print(y)

    # 방법
    # while x:
    #     # 왼쪽으로 가는 경우(현재 진행방향이 위 또는 왼쪽, 즉 현재 진행방향이 오른쪽이 아닐때)
    #     if check(x, y - 1):
    #         while check(x, y - 1):
    #             y -= 1
    #         x -= 1
    #     # 오른쪽으로 가는 경우(현재 진행방향이 위 또는 오른쪽, 즉 현재 진행방향이 왼쪽이 아닐때)
    #     elif check(x, y + 1):
    #         while check(x, y + 1):
    #             y += 1
    #         x -= 1
    #     # 그외(위로 가는 경우)
    #     else:
    #         x -= 1
    # print(y)
    #
    #
    # 방법
    # while x:
    #     arr[x][y] = 0
    #     # 왼쪽으로 가는 경우(현재 진행방향이 위 또는 왼쪽, 즉 현재 진행방향이 오른쪽이 아닐때)
    #     if check(x, y - 1):
    #         y -= 1
    #     # 오른쪽으로 가는 경우(현재 진행방향이 위 또는 오른쪽, 즉 현재 진행방향이 왼쪽이 아닐때)
    #     elif check(x, y + 1):
    #         y += 1
    #     # 그외(위로 가는 경우)
    #     else:
    #         x -= 1
    # print(y)
    #
    #
    # # 방법
    # ans = 0
    # ladder(x, y)
    # print(ans)
    #
    # 방법
    print(ladder2(x, y))