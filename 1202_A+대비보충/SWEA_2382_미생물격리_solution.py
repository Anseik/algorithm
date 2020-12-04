import sys
sys.stdin = open('SWEA_2382_미생물격리.txt')


T = int(input())
for tc in range(1, T + 1):
    # N : 구역 크기, M : 격리 시간, K : 군집 개수
    N, M, K = map(int, input().split())
    groups = []
    for k in range(K):
        r, c, cnt, dir = map(int, input().split())
        groups.append([r, c, cnt, dir])


