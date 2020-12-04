import sys
sys.stdin = open('전봇대.txt')

def comb(idx, cnt, select):
    global result
    if cnt == 2:
        s1, e1, s2, e2 = 0, 0, 0, 0
        for i in range(N):
            if select[i] == 1:
                if not s1:
                    s1, e1 = arr[i]
                else:
                    s2, e2 = arr[i]
                    break
        # 교차 : 시작점은 낮고 끝점은 높거나 / 시작점은 높고 끝점은 낮다
        if (s1 < s2 and e1 > e2) or (s1 > s2 and e1 < e2):
            result += 1
        return

    if idx == N:
        return

    select[idx] = 1
    comb(idx + 1, cnt + 1, select)
    select[idx] = 0
    comb(idx + 1, cnt, select)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        s, e = map(int, input().split())
        arr.append((s, e))
    # print(arr)

    result = 0
    select = [0] * N
    comb(0, 0, select)

    print("#{} {}".format(tc, result))