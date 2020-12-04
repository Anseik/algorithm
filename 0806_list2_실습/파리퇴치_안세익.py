import sys
sys.stdin = open('파리퇴치.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # print(arr)

    max_fly = 0
    # 모든 사각영역의 좌상단 좌표
    for r in range(N-M+1):
        for c in range(N-M+1):

            sum_fly = 0
            # 좌상단 좌표가 (r, c)이고 크기가 M인 사각영역
            for i in range(M):
                for j in range(M):
                    sum_fly += arr[r+i][c+j]
            if sum_fly > max_fly:
                max_fly = sum_fly

    print('#%d' %tc, max_fly)

