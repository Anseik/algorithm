import sys
sys.stdin = open('view.txt')

T = 10
for tc in range(1, T+1):
    N = int(input()) # 가로 길이
    building = list(map(int, input().split())) # 빌딩들에 대한 정보
    # print(N)
    # print(building)

    # 왼쪽, 오른쪽 두칸씩 비어있으면 조망권이 확보된것, 조망권이 확보된 세대수?
    # 순회하면서 i-2, i-1, i+1, i+2보다 높이가 높을때 그 중에 가장 높은것보다 얼마나 높은지 카운트

    cnt = 0
    for i in range(2, N-2):
        tmp = max(building[i-2], building[i-1], building[i+1], building[i+2])
        if building[i] > tmp:
            cnt += (building[i] - tmp)

    print("#{} {}".format(tc, cnt))

