import sys
sys.stdin = open('농작물 수확하기.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    result = 0
    for r in range(N):
        sp = abs(N // 2 - r)
        for c in range(sp, sp + (N - 2 * sp)):
            result += farm[r][c]

    print("#{} {}".format(tc, result))
