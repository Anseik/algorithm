# 최소힙
tmp = [7, 2, 4, 3, 1, 6, 5]
size = len(tmp)
heap = [0] * (size + 1)
heapcount = 0 # 현재 마지막 노드가 들어 있는 인덱스

def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value

    # 만약에 새롭게 정의된 자식이 부모노드보다 작으면,
    # 부모노드와 위치를 바꿔줘야 한다.
    cur = heapcount
    parent = cur // 2
    # 부모노드가 현재 노드보다 작거나 부모노드가 없을때 까지(즉 루트일때까지) 계속반복
    while parent and heap[cur] < heap[parent]:
        heap[cur], heap[parent] = heap[parent], heap[cur]
        cur = parent
        parent = cur // 2


def heappop():
    global heapcount
    result = heap[1] # root를 없애기전 저장(반환해야 하니까)

    # heap의 마지막 인덱스에 있는 노드를 root로 바꿔준다
    # 마지막 노드는 기존에 추가되어 있는 노드에 영향을 미치지 않기때문이다.
    heap[1] = heap[heapcount]
    heap[heapcount] = 0
    heapcount -= 1 # 마지막노드를 없앤다.

    # 자식들 중에서 가장 작은 애가 부모가 되어야 한다.
    parent = 1
    child = 2 * parent # 왼쪽 자식을 초기값으로 오른쪽 자식과 비교하여 더 작은 것 선택
    if child + 1 <= heapcount and heap[child + 1] < heap[child]:
        child = child + 1

    # 만약에 자식과 부모노드를 비교해서 자식노드가 더 작으면 swap
    while child <= heapcount and heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
        child = 2 * parent
        if child + 1 <= heapcount and heap[child + 1] < heap[child]:
            child = child + 1

    return result

for i in tmp:
    heappush(i)
print(heap)

for i in range(size):
    print(heappop(), end = " ")
print()