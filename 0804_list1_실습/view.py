import sys
sys.stdin = open('view.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    total = 0 # 전체 조망권
    for i in range(2, N-2):
        # print(buildings[i], end=' ')
        # 왼쪽 조망권 구하고
        # 옆, 옆옆 건물의 높이 중 큰 값 선택
        left = 0
        left_view = 0
        if buildings[i-1] > buildings[i-2]:
            left = buildings[i-1]
        else:
            left = buildings[i-2]

        left_view = buildings[i] - left

        # 오른쪽 조망권 구하고
        right = 0
        right_view = 0
        if buildings[i+1] > buildings[i+2]:
            right = buildings[i+1]
        else:
            right = buildings[i+2]

        right_view = buildings[i] - right

        # 조망권이 없는 경우는 넘어간다.
        if left_view <= 0 or right_view <= 0:
            continue

        # 작은값 선택해서 전체 조망권(total)에 더한다.
        if left_view > right_view:
            total += right_view
        else:
            total += left_view

    print("#{} {}".format(tc, total))

