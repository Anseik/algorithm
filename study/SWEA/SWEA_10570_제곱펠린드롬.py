import sys
sys.stdin = open('SWEA_10570_제곱펠린드롬.txt')

def pal_cnt(num):
    global cnt
    num = str(num)
    N = len(num)
    M = N // 2
    for i in range(M):
        if num[i] == num[N - 1 - i]:
            continue
        return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    # print(A, B)

    cnt = 0
    for num in range(A, B + 1):
        if pal_cnt(num):
            sr = str(num ** 0.5)
            idx = 0
            for i in range(len(sr)):
                if sr[i] == '.':
                    idx = i
                    break
            # print(idx)
            if sr[idx + 1] == '0' and (idx + 2) == len(sr):
                if pal_cnt(int(float(sr))):
                    cnt += 1



    print("#{} {}".format(tc, cnt))

