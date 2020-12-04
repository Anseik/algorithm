import sys
sys.stdin = open('boj_4195_친구네트워크.txt')

# def dfs(name):
#     global cnt
#     visit.append(name)
#     cnt += 1
#     f_list = G[name]
#     N = len(f_list)
#     for j in range(N):
#         if not f_list[j] in visit:
#             dfs(f_list[j])

def bfs(name):
    global cnt
    visit.append(name)
    Q = []
    Q.append(name)
    cnt += 1
    while Q:
        p = Q.pop(0)
        f_list = G[p]
        N = len(f_list)
        for j in range(N):
            if not f_list[j] in visit:
                visit.append(f_list[j])
                Q.append(f_list[j])
                cnt += 1

T = int(input())
for tc in range(1, T + 1):
    F = int(input())
    G = {}
    for i in range(F):
        p1, p2 = input().split()
        # print(p1, p2)
        if p1 in G:
            G[p1].append(p2)
        else:
            G[p1] = [p2]
        if p2 in G:
            G[p2].append(p1)
        else:
            G[p2] = [p1]

        visit = []
        cnt = 0
        bfs(p1)
        print(cnt)
