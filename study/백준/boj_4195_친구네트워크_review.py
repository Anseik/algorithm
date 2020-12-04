import sys
sys.stdin = open('boj_4195_친구네트워크.txt')

# 최상위 부모(root)를 찾는 함수
def find(x):
    if parents[x] == x: # 기저영역(root)
        return x
    p = find(parents[x]) # root를 찾을때까지 재귀호출한다.
    parents[x] = p # 트리를 압축한다.(트리의 높이를 줄이기 위함)
    return p

# 친구관계를 맺은 두 사람이 부모가 다르면 네트워크를 연결해줘야한다.
def union(f1, f2):
    p1 = find(f1)
    p2 = find(f2)
    if p1 != p2:
        parents[p2] = p1
        nets[p1] += nets[p2]

T = int(input())
for tc in range(1, T + 1):
    F = int(input())
    parents = {}
    nets = {}
    for _ in range(F):
        f1, f2 = input().split()
        if f1 not in parents:
            parents[f1] = f1
            nets[f1] = 1
        if f2 not in parents:
            parents[f2] = f2
            nets[f2] = 1
        union(f1, f2)
        # print(parents)
        # print(nets)
        print(nets[find(f1)])