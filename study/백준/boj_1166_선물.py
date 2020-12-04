import sys
sys.stdin = open('boj_1166_선물.txt')

def binary_search(s, e):
    global result
    for i in range(10000):
        m = (s + e) / 2
        # 한변의 길이가 m인 작은 상자 N개를 큰 상자에 넣을 수 있는 경우
        inner_cnt = (L // m) * (W // m) * (H // m)
        if inner_cnt >= N:
            result = m
            s = m
        # 넣을 수 없는 경우
        else:
            e = m


N, L, W, H = map(int, input().split())
# print(N, L, W, H)
result = 0
binary_search(0, min(L, W, H))

print(result)



