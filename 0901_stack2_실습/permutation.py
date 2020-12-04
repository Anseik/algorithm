# permutation(순열)
arr = [1, 2, 3, 4, 5]
N = len(arr)

def perm(idx):
    if idx == N:
        print(arr)
        return
    # 현재 idx에서 해야할 모든 경우의 수
    # 나보다 뒤쪽에 있는 모든 요소들과 자리 바꾸기
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]

perm(0)