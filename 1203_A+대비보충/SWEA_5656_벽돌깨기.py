import sys
sys.stdin = open('SWEA_5656_벽돌깨기.txt')

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    print(N, W, H)
    print(arr)