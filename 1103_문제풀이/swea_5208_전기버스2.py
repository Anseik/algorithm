import sys
sys.stdin = open('swea_5208_전기버스2.txt')


def solve(select, idx, cnt, power):
    # idx 정류장 번호, cnt, 배터리 교환횟수, power 현재위치에서 남은 배터리량
    global min_cnt
    if cnt >= min_cnt:
        return
    if idx == N: # 종점에 도착하면
        if min_cnt > cnt:
            min_cnt = cnt
        return
    # 교환을 하면 그 정류장에 있었던 배터리크기 - 1로 power를 변경
    select[idx] = 1
    solve(select, idx + 1, cnt + 1, powers[idx] - 1)
    # 교체하지 않으면 idx를 이동할때 마다 배터리를 1감소
    # power가 0보다 클때만 배터리를 교체하지 않을 수 있다.
    if power > 0:
        select[idx] = 0
        solve(select, idx + 1, cnt, power - 1)
T = int(input())
for tc in range(1, T + 1):
    powers = list(map(int, input().split()))
    N = powers[0]

    select = [0] * N
    min_cnt = N - 1
    power = powers[1]
    solve(select, 2, 0, power-1)
    print('#{} {}'.format(tc, min_cnt))

