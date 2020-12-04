# 모든 경우의 수에서 답이될 가능성이 없는 경우를 제외
# 직원들이 선택된 일을 했을때 전체 성공확률이 최대가 되도록 해야한다.
import sys
sys.stdin = open('swea_1865_동철이의일분배_solution.txt')

# 성공확률을 곱할때 마다 확률은 줄어든다(0 <= 확률 <= 1)
# 중간 결과가 정답 후보보다 이미 작으면 그 선택은 더 이상 계산할 필요가 없다.
# rate : 중간 결과
def solve(idx, rate):
    global max_rate
    if rate <= max_rate:
        return
    if idx == N:
        max_rate = max(max_rate, rate)
        return
    for i in range(N):
        if not selected[i] and arr[idx][i]:
            selected[i] = 1
            solve(idx + 1, rate * arr[idx][i])
            selected[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(lambda x: x / 100, list(map(int, input().split())))) for _ in range(N)]
    # print(N)
    # print(arr)
    selected = [0] * N
    max_rate = 0
    solve(0, 1)
    # print(max_rate)
    result = format(max_rate * 100, '.6f')
    print('#{} {}'.format(tc, result))