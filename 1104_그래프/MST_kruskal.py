import heapq

# 그래프 입력받기
'''
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 6 25
2 4 46
3 5 18
3 4 34
4 6 51
4 5 40
'''

# 요소 x가 포함되는 집합의 대표자를 반환하는 함수
def find_set(x):
    # 요소와 요소의 부모가 일치하면 해당 요소가 집합의 대표자이다.
    if x == parent[x]:
        return x
    else:
        p = find_set(parent[x])
        parent[x] = p # 트리 압축
        return p


# x와 y가 포함되는 잡합의 대표자를 하나로 만들어줌(집합을 합치는 것과 동일)
def union(x, y):
    # x와 y의 대표자가 같을때(같은 집합일때) 아무 작업 안함
    # x와 y의 대표자가 다를때(다른 집합일때) 대표자를 같게 만들어준다(집합을 합친다.)
    a = find_set(x)
    b = find_set(y)
    if a == b:
        return
    else:
        # b의 대표자를 a로 만들어준다.
        parent[b] = a


def kruskal(queue):
    mst = list()
    while queue:
        weight, v = heapq.heappop(queue)
        if find_set(v[0]) == find_set(v[1]): # 이미 대표자가 같으면 넘어간다.
            continue
        union(v[0], v[1])
        mst.append((v, weight))

    return mst


V, E = map(int, input().split())
queue = list()
parent = list(range(V))
for i in range(E):
    s, e, w = map(int, input().split())
    # 가중치를 기준으로 정렬
    # heapq(priority queue) 기준을 설정해주면 우선되는 요소가 먼저 pop
    # 가중치가 작은 것부터 꺼내와서 mst에 연결할 수 있는지 검사
    # heappush(대상 queue, 요소) : 요소의 첫번째 값이 기준이 된다.
    heapq.heappush(queue, (w, (s, e)))

result = kruskal(queue)
min_sum = 0
for j in range(len(result)):
    min_sum += result[j][1]
print(result)
print(min_sum)




