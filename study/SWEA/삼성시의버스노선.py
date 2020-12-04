import sys
sys.stdin = open('삼성시의버스노선.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lines = []
    for _ in range(N):
        a, b = map(int, input().split())
        lines.append([a, b])
    # print(lines)

    P = int(input())
    stops  = []
    for _ in range(P):
        c = int(input())
        stops.append(c)
    # print(stops)

    cnt = [0] * P
    for i in range(P):
        for j in range(N):
            if lines[j][0] <= stops[i] <= lines[j][1]:
                cnt[i] += 1

    print("#{}".format(tc), end=" ")
    print(*cnt)
