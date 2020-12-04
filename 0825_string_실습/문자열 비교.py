import sys
sys.stdin = open('문자열 비교.txt')

T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()
    m = len(p)
    n = len(t)

    def brute(p, t):
        for i in range(n - m + 1):
            for j in range(m):
                if p[j] != t[j+i]:
                    break
            else:
                return 1
        else:
            return 0

    result = brute(p, t)

    print("#{} {}".format(tc, result))