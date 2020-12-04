import sys
sys.stdin = open('전기버스.txt')

T = int(input())
for tc in range(1, T+1):
    # K : 최대 이동 가능거리
    # N : 정류장 거리(종점)
    # M : 충전기 정류장 개수
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    # print(K, N, M)
    # print(station)

    stations.insert(0, 0)
    stations.append(N)
    # print(stations)

    pos = 0 # 버스 위치
    cnt = 0 # 충전 횟수
    for i in range(1, M+2): # 앞뒤로 시작과 종료지점을 추가해서 + 2
        # 현재 정류장의 위치와 이전 정류장의 위치 차가 K보다 크다면, 충전불가능
        if (stations[i] - stations[i-1]) > K:
            cnt = 0
            break
        # 충전 하려고 하는 정류장의 위치가 pos+K 보다 크다면
        # 이전 정류장에서 충전을 해야함
        if (stations[i] > pos + K):
            pos = stations[i-1]
            cnt += 1

    print('#%d' %tc, cnt)