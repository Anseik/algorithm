import sys
sys.stdin = open('회전.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(N, M)
    # print(arr)

    for _ in range(M):
        tmp = arr.pop(0)
        arr.append(tmp)

    result = arr.pop(0)
    print("#{} {}".format(tc, result))