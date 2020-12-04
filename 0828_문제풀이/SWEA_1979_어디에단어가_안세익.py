import sys
sys.stdin = open('SWEA_1979_어디에단어가_안세익.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # print(puzzle)

    result = 0
    for r in range(N):
        cnt = 0
        for c in range(N):
            if puzzle[r][c] == 1:
                cnt += 1

            if puzzle[r][c] == 0 or c == N-1: # 0이 나오면, 길이 검사 후 길이를 0으로 만듬
                if cnt == M: # stack의 길이를 검사
                    result += 1
                cnt = 0 # stack이 빌때까지 pop

    for r in range(N):
        cnt = 0
        for c in range(N):
            if puzzle[c][r] == 1:
                cnt += 1

            if puzzle[c][r] == 0 or c == N-1:
                if cnt == M:
                    result += 1
                cnt = 0

    print("#{} {}".format(tc, result))