import sys
sys.stdin = open('부분집합의합.txt')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(A)
power_set = []
for i in range(1 << n):
    sub_set = []
    for j in range(n):
        if i & (1 << j):
            sub_set.append(A[j])
    power_set.append(sub_set)

# print(power_set)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # print(N, K)

    cnt = 0
    for i in range(len(power_set)):
        if len(power_set[i]) == N and sum(power_set[i]) == K:
            cnt += 1

    print("#{} {}".format(tc, cnt))

