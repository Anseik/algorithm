import sys
sys.stdin = open('배열최소합.txt')

def perm(k, cur_sum): # cur_sum: 0 ~ k - 1 행에 선택한 값들의 합
    global ans
    if ans <= cur_sum: return

    if k == N:
        ans = min(ans, cur_sum)

    else:
        for i in range(k, N): # 사용할 수 있는 열의 모든 경우의 수(순열)
            cols[k], cols[i] = cols[i], cols[k]
            perm(k + 1, cur_sum + arr[k][cols[k]]) # cols[k]는 k행에서 선택한 열의 인덱스를 의미
            cols[k], cols[i] = cols[i], cols[k]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cols = [i for i in range(N)]
    ans = 0xffffff

    perm(0, 0)
    print(ans)