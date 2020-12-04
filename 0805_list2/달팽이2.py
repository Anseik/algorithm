import sys
sys.stdin = open('달팽이_solution.py')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # print(arr)

    #     우  하  좌  상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = 0
    c = 0
    arr[r][c] = 1

    for num in range(2, N*N+1):
        # 델타 순서가 우하좌상이기 때문에 달팽이가 위로가야되는 상황인데 오른쪽으로 가는 경우가 생겨 c == 0일때는 항상 위를 먼저 탐색하도록 코드 추가
        if c == 0:
            r = r + dr[-1]
            c = c + dc[-1]
            if 0 <= r < N and 0 <= c < N:
                if arr[r][c] == 0:
                    arr[r][c] = num
                    continue # 숫자가 채워지면 아래 for문으로 들어가면 안되므로 continue
                # 숫자가 채워지지 않으면 r,c를 다시 원상태로 돌려놔야함
                else:
                    r = r - dr[-1]
                    c = c - dc[-1]
            else:
                r = r - dr[-1]
                c = c - dc[-1]

        for i in range(4):
            r = r + dr[i]
            c = c + dc[i]
            if 0 <= r < N and 0 <= c < N:
                if arr[r][c] == 0:
                    arr[r][c] = num
                    break # 숫자가 채워지면 for문을 더 이상 반복할 필요가 없으므로 break
                else:
                    r = r - dr[i]
                    c = c - dc[i]
            else:
                r = r - dr[i]
                c = c - dc[i]

    print('#%d' %tc)
    for r in range(N):
        for c in range(N):
            print(arr[r][c], end=" ")
        print()