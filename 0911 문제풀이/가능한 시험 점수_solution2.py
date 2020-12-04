import sys
sys.stdin = open('가능한 시험 점수.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))

    # dfs를 이용한 방법
    # visit = [[0] * (sum(score) + 1) for _ in range(N + 1)]      # 레벨 별로 중복을 제거
    #
    # def dfs(k, s): # k는 0 ~ N - 1까지, s는 점수의 합
    #     if visit[k][s]: return
    #     visit[k][s] = 1
    #     if k == N: return
    #
    #     dfs(k + 1, s) # k번 문제를 틀린 경우
    #     dfs(k + 1, s + score[k]) # k번 문제를 맞은 경우
    #
    # dfs(0, 0)
    # print(sum(visit[N]))

    # bfs를 이용한 방법
    # visit = [0] * (sum(score) + 1)
    # Q = [[0, 0]] # k: 레벨, s: 점수
    # while Q:
    #     k, s = Q.pop(0)
    #     if k == N:
    #         visit[s] = 1
    #     else:
    #         Q.append([k + 1, s])
    #         Q.append([k + 1, s + score[k]])
    # print(sum(visit))

    # bfs를 이용한 방법(중복제거)
    visit = [0] * (sum(score) + 1)
    Q = [0]
    visit[0] = 1
    for val in score:
        for i in range(len(Q)):
            if visit[Q[i] + val]: continue
            visit[Q[i] + val] = 1
            Q.append(Q[i] + val)
    print(len(Q))
