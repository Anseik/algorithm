import sys
sys.stdin = open('햄버거 다이어트.txt')

def powerset(idx, taste, cal):
    global max_taste
    if cal > L:
        return
    if idx == N:
        if taste > max_taste:
            max_taste = taste
        return
    powerset(idx + 1, taste + ingre[idx][0], cal + ingre[idx][1] )
    powerset(idx + 1, taste, cal)

T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    ingre = [list(map(int, input().split())) for _ in range(N)]

    max_taste = 0
    powerset(0, 0, 0)

    print("#{} {}".format(tc, max_taste))
