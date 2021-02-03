# 원소가 3개인 부분집합을 구하여라

arr = [6, 5, 3, 1, 4]
N = len(arr)
selected = [0] * N
T = 3

def comb(selected, idx, cnt):
    # 리턴 조건
    if cnt == T:
        subset = []
        for i in range(N):
            if selected[i] == 1:
                subset.append(arr[i])
        print(subset)
        return
    if idx == N:
        return
    selected[idx] = 1
    comb(selected, idx + 1, cnt + 1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)

comb(selected, 0, 0)