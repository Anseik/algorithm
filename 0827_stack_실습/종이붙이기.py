import sys
sys.stdin = open('종이붙이기.txt')

def cnt_case(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return cnt_case(N-10) + cnt_case(N-20)*2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = cnt_case(N)

    print("#{} {}".format(tc, result))