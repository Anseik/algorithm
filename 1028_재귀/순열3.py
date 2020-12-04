def perm(n, k, m): # n 숫자를 결정할 자리(인덱스), k 순열의 길이, m 주어진 숫자의 개수

    if n == k:
        print(p)
    else:
        for i in range(m):
            if u[i] == 0: # A[i]가 사용전이면
                u[i] = 1
                p[n] = A[i]
                perm(n+1, k, m)
                u[i] = 0


A = [1, 2, 3, 4, 5]
p = [0] * 3
u = [0] * 5
perm(0, 3, 5)