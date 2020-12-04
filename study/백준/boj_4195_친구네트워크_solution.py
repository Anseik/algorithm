# 분리집합 문제
import sys
sys.stdin = open('boj_4195_친구네트워크.txt')

def find(x):
    if parents[x] == x: # 가장 최상단의 부모 노드를 찾아서 리턴
        return x

    p = find(parents[x])
    parents[x] = p  # 부모를 갱신해줌 트리를 압축
    return p


def union(person1, person2, cnt):
    a = find(person1)
    b = find(person2)

    if a != b:
        parents[b] = a
        cnt[a] += cnt[b]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    parents = {}
    cnt = {}
    for i in range(n):
        p1, p2 = input().split()
        if p1 not in parents:   # 각각을 집합처럼 저장
            parents[p1] = p1
            cnt[p1] = 1
        if p2 not in parents:
            parents[p2] = p2
            cnt[p2] = 1
        union(p1, p2, cnt)  # 부모 노드를 찾아서 이름과 cnt를 저장해준다.
        print(parents)
        print(cnt)
        print(cnt[find(p1)])