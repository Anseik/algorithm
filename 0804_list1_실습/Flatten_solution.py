import sys
sys.stdin = open('Flatten.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    area = list(map(int, input().split()))

    for i in range(N):
        max_idx = 0
        min_idx = 0
        max_v = area[0]
        min_v = area[0]
        for j in range(len(area)):
            if area[j] > max_v:
                max_v = area[j]
                max_idx = j
            if area[j] < min_v:
                min_v = area[j]
                min_idx = j

        area[max_idx] -= 1
        area[min_idx] += 1

    result = max(area) - min(area)
    print("#{} {}".format(tc, result))
