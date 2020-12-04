arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
subset = list()
def powerset(subset, idx):
    if idx == N:
        if sum(subset) == 0:
            print(subset)

        return

    # idx번째 요소가 선택된 경우
    subset.append(arr[idx])
    powerset(subset, idx + 1)

    # 선택되지 않은 경우
    subset.pop()
    powerset(subset, idx + 1)

powerset(subset, 0)
