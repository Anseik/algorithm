# permutation(순열)
arr = [1, 2, 3, 4, 5]
N = len(arr)


def perm(idx):
    if idx == N:
        print(arr)
        return
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx]


perm(0)
