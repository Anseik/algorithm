import sys
sys.stdin = open('SWEA_중위순회.txt')

def in_order(i):
    if i > N:
        return
    in_order(2 * i) # 왼쪽 자식
    result.append(tree[i])
    in_order(2 * i + 1) # 오른쪽 자식

T = 10
for tc in range(1, T+1):
    N = int(input())
    info = [input().split() for _ in range(N)]

    # 해당 하는 노드번호(인덱스)에 텍스트를 저장
    tree = [0] * (N + 1)
    for i in range(N):
        node, text, *child = info[i] # 가변인자 리스트 활용
        tree[int(node)] = text

    result = []
    in_order(1)
    answer = "".join(result)
    print("#{} {}".format(tc, answer))