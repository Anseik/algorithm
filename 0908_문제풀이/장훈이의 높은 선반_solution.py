import sys
sys.stdin = open('장훈이의 높은 선반.txt')

def tower(idx, tmp_sum):
    global min_height

    if tmp_sum > min_height:
        return

    if idx == N:
        # 키의 합이 B가 넘는 경우에만 정답이 될 수 있다.
        if B <= tmp_sum < min_height:
            min_height = tmp_sum
        return

    tower(idx + 1, tmp_sum + heights[idx])
    tower(idx + 1, tmp_sum)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    INF = float('inf')
    min_height = INF
    tower(0, 0)
    result = min_height - B
    print("#{} {}".format(tc, result))