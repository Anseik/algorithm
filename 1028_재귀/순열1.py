def perm(n, k): # n 숫자를 결정할 인덱스 / k 순열의 길이
    if n == k:
        print(A)
    else:
        for i in range(n, k):
            A[n], A[i] = A[i], A[n]
            perm(n + 1, k)
            A[n], A[i] = A[i], A[n]


A = [1, 2, 3]

perm(0, 3)