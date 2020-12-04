import sys
sys.stdin = open('이진탐색.txt')

def in_order(v):
    global number
    if v <= N:
        in_order(2 * v)
        tree[v] = number
        number += 1
        in_order(2 * v + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # print(N)

    tree = [0] * (N + 1)
    number = 1
    in_order(1)
    root = tree[1]
    answer = tree[N // 2]
    print("#{} {} {}".format(tc, root, answer))