arr = [1, 2, 3, 4, 5]
N = len(arr)
used = [0] * N
perm_arr = [0] * N

def perm(used, perm_arr, idx):
    if idx == N:
        print(perm_arr)
        return

    for i in range(N):
        if not used[i]:
            perm_arr[idx] = arr[i]
            used[i] = 1
            perm(used, perm_arr, idx + 1)
            used[i] = 0

perm(used, perm_arr, 0)