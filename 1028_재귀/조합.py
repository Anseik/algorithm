def f(n, s, N, r): # n : 조합의 인덱스, s : 선택구간의 시작, N : 주어진 개수, r : 고를 개수
    if n == r:
        print(c)
    else:
        for i in range(s, N-r+n+1): # 고를 수 있는 범위 s ~ N - r + n
            c[n] = i
            f(n+1, i+1, N, r)

N = 10
r = 3
c = [0] * 3
f(0, 0, N, r)