import sys
sys.stdin = open('부분집합.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = []
    for i in range(1, 13):
        A.append(i)
    # print(A)

    power_set =[]
    for j in range(1<<len(A)): # 부분집합의 개수
        set = []
        for k in range(len(A)): # 원소의 개수
            if j & (1<<k): # j의 k번째 자리가 1이면
                set.append(A[k])
        power_set.append(set)

    # print(power_set)

    cnt = 0
    for l in range(len(power_set)):
        n = 0
        k = 0
        for m in range(len(power_set[l])):
            n += 1
            k += power_set[l][m]
        if n == N and k == K:
            cnt += 1

    print('#%d' %tc, cnt)
