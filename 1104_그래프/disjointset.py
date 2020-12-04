N = 5
parent = list(range(N + 1))

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

print(parent)
union(0, 1)
union(2, 3)
union(4, 5)
print(parent)
union(1, 5)
print(parent)