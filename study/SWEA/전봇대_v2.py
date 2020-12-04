import sys
sys.stdin = open('전봇대.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        s, e = map(int, input().split())
        arr.append((s, e))
    # print(arr)

    result = 0
    for i in range(N):
        s1, e1 = arr[i]
        for j in range(i, N):
            s2, e2 = arr[j]
            if (s1 < s2 and e1 > e2) or (s1 > s2 and e1 < e2):
                result += 1

    print("#{} {}".format(tc, result))