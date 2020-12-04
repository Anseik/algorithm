arr = [3, 2, 5, 1, 4]
N = 5

for j in range(N - 1):
    # 1. 가장 작은 요소를 찾는다.
    min_v = arr[j]
    min_idx = j
    for i in range(j, N):
        if min_v > arr[i]:
            min_v = arr[i]
            min_idx = i

    # 2. 가장 작은 요소를 가장 앞 요소와 자리를 바꾼다.
    arr[j], arr[min_idx] = arr[min_idx], arr[j]

print(arr)


