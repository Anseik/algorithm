import sys
sys.stdin = open('다솔이의월급상자.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = 0
    for i in range(N):
        p, x = map(float, input().split())
        multi = p * x
        result += multi

    ans = format(result, ".6f")
    print("#{} {}".format(tc, ans))