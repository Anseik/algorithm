arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
A = [0] * N

def powerset(n, k, cursum):
    if cursum > 10: return
    if n == k:
        print(A, end=" ")
        for i in range(n):
            if A[i] == 1:
                print(arr[i], end=" ")
        print()
    else:
        # k번째 요소 포함
        A[k] = 1
        powerset(n, k+1, cursum + arr[k])
        # k번째 요소 미포함
        A[k] = 0
        powerset(n, k+1, cursum)

powerset(N, 0, 0)