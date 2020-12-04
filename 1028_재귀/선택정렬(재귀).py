# 재귀를 이용한 반복문
arr = [3, 2, 5, 1, 4]
N = 5

def selection_sort(idx):
    if idx >= N - 1:
        return
    # 현재 요소 이후에 있는 요소들 중에 가장 작은 값을 찾아서 현재요소와 자리를 바꾼다.
    # 1. 가장 작은 요소를 찾는다.
    min_v = arr[idx]
    min_idx = idx
    for i in range(idx, N):
        if min_v > arr[i]:
            min_v = arr[i]
            min_idx = i

    # 2. 가장 작은 요소를 가장 앞 요소와 자리를 바꾼다.
    arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    selection_sort(idx + 1) # 다음요소 정렬을 위한 호출

# selection_sort(0)
# print(arr)

# ---------------------------------------------------------------------------------

def min_value(idx):
    if idx == N - 1:
        return (arr[N - 1], idx)
    # 이후에 요소들 중 최소값을 반환하는 재귀 호출과 현재 요소 중
    # 작은 값을 반환하면 됨
    tmp = min_value(idx + 1)
    if arr[idx] < tmp[0]:
        return (arr[idx], idx)
    else:
        return tmp


def selection_sort2(idx):
    if idx >= N - 1:
        return
    # 현재 요소 이후에 있는 요소들 중에 가장 작은 값을 찾아서 현재요소와 자리를 바꾼다.
    # 1. 가장 작은 요소를 찾는다.
    min_v, min_idx = min_value(idx)
    # 2. 가장 작은 요소를 가장 앞 요소와 자리를 바꾼다.
    arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    # print(arr)
    selection_sort2(idx + 1) # 다음요소 정렬을 위한 호출

selection_sort2(0)
print(arr)

