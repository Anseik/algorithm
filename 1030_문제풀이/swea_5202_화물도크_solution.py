import sys
sys.stdin = open('swea_5202_화물도크_solution.txt')


T = int(input())
for tc in range(1, T + 1):
    # 신청서의 개수
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    # 종료 시간 순으로 정렬
    jobs.sort(key = lambda x: x[1])

    ans = 1
    finish = jobs[0][1]

    for i in range(1, N):
        if jobs[i][0] >= finish:
            ans += 1
            finish = jobs[i][1]

    print('#{} {}'.format(tc, ans))
