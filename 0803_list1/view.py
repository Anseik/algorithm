import sys
sys.stdin = open('input.txt')

for i in range(1, 11):
    a = int(input())
    b = list(map(int, input().split()))

    cnt = 0
    for j in range(2, a-2):
        max_height = max(b[j-2], b[j-1], b[j+1], b[j+2])
        if b[j] > max_height:
            cnt += (b[j] - max_height)

    print('#{} {}'.format(i, cnt))
