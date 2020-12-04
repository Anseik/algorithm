import sys
sys.stdin = open('문자열비교.txt')

T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()
    # print(p)
    # print(t)
    N = len(t)
    M = len(p)

    result = 0
    for i in range(N-M+1):
        for j in range(M):
            if p[j] != t[i+j]:
                break
        else:
            result = 1
            break

    print("#{} {}".format(tc, result))