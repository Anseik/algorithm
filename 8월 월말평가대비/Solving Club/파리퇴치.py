import sys
sys.stdin = open('파리퇴치.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M)
    # print(arr)

    result = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            fly = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    fly += arr[i][j]
            if fly > result:
                result = fly

    print("#{} {}".format(tc, result))