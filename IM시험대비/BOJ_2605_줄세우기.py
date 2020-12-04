import sys
sys.stdin = open('BOJ_2605_줄세우기.txt')

T = 1
for tc in range(1, T + 1):
    N = int(input())
    picks = list(map(int, input().split()))
    line = [i for i in range(1, N + 1)]
    for idx in range(N):
        np = idx - picks[idx] # 새로운 자리의 인덱스는 기존자리의 인덱스에서 뽑은 번호만큼 뺀것
        line.insert(np, line.pop(idx)) # 팝해서 새로운 자리에 삽입한다.
    print(*line)