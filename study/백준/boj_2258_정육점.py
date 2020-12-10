import sys
sys.stdin = open('boj_2258_정육점.txt')

N, M = map(int, input().split())
# print(N, M)

meats = []
for i in range(N):
    weight, cost = map(int, input().split())
    # print(weight, cost)
    meats.append((weight, cost))

# 가격기준 오름차순 정렬, 가격이 같으면 무게가 큰것 먼저
meats.sort(key=lambda x: (x[1], -x[0]))
# print(meats)

for i in range(N):
    total = meats[i][0]
    cost = meats[i][1]
    for j in range(0, i):
        if meats[j][1] < cost:
            total += meats[j][0]
    if total >= M:
        print(cost)
        break
else:
    print(-1)


