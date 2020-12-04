arr = [6, 5, 3, 1, 4]
N = len(arr)
selected = [0] * N
T = 3

def comb(selected, idx, cnt):
    # idx가 범위를 벗어나거나, 원하는 만큼의 요소를 이미 선택했을 때 더이상 진행 안함
    if cnt == T: # 필요한 개수만큼 선택함
        for i in range(N):
            if selected[i] == 1:
                print(arr[i], end=" ")
        print()
        return
    if idx == N: # 범위 벗어남
        return

    # 요소의 포함/미포함 여부 결정
    selected[idx] = 1
    comb(selected, idx + 1, cnt + 1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)

# 부분 집합중에 요소의 개수가 특정 수인 집합
# [6, 5, 3, 1, 4]의 부분집합 에서 요소의 개수가 3개인 부분집합 구하기


comb(selected, 0, 0)