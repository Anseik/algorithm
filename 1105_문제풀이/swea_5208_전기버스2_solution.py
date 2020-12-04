import sys
sys.stdin = open('swea_5208_전기버스2_solution.txt')


# idx : 정류장 번호 / cnt : 배터리 교환횟수 / remain : 배터리 잔량
def backtrack(idx, cnt, remain):
    global min_cnt
    # 다음 정류장 도착하면 remain -1
    remain -= 1
    if cnt >= min_cnt:  # 중간 배터리 교환 횟수가 정답후보 이상이면 리턴
        return
    if idx == N:
        min_cnt = cnt
        return
    # 배터리를 교환하는 경우
    backtrack(idx + 1, cnt + 1, arr[idx])
    # 배터리를 교환하지 않는 경우(배터리 잔량이 남아있어야만 교환하지 않을 수 있다.)
    if remain > 0:
        backtrack(idx + 1, cnt, remain)


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]

    min_cnt = 0xffffffff
    backtrack(2, 0, arr[1])
    print('#{} {}'.format(tc, min_cnt))

