# import sys
# sys.stdin = open('Algo2_구미_1반_안세익.txt')


def comb(select, before, idx, cnt, cursum):
    # before : 이전에 돌을 밟았으면 1, 밟지 않았으면 0, 출발할때는 -1로 초기화
    # cursum : 현재까지 밟은 돌의 점수의 합
    global max_num
    if idx == N: # 모든 요소의 선택여부가 결정되었을때
        # 돌을 M번 밟았고 점수가 더 크면
        if cnt == M and max_sum < cursum:
            max_sum = cursum
            return
        return

    # 돌을 밟는 횟수가 M을 초과하면 조건에 부합하지 않으므로 return
    if cnt > M:
        return

    # 이번 돌을 밟는다.
    select[idx] = 1
    comb(select, 1, idx + 1, cnt + 1, cursum+stones[idx])

    # 이전 돌을 밟지 않았으면 이번 돌은 밟아야 한다.(연속된 두 개의 돌을 뛰어 넘을 수 없다.)
    # 이전 돌을 밟았을 때만 이번 돌을 밟지 않을 수 있다.
    if before != 0:
        # 이번 돌을 밟지 않는다.
        select[idx] = 0
        comb(select, 0, idx + 1, cnt, cursum)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))
    # print(N, M)
    # print(stones)

    max_num = 0
    select = [0] * N
    # 매개변수 : select, before, idx, cnt, cursum
    comb(select, -1, 0, 0, 0)

    print('#{} {}'.format(tc, max_num))

