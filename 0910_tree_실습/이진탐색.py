import sys
sys.stdin = open('이진탐색.txt')

def in_order(idx):
    global num
    if idx > N:
        return
    in_order(2 * idx)
    tree[idx] = num
    num += 1
    in_order(2 * idx + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # print(N)

    num = 1
    tree = [0] * (N + 1)
    in_order(1)
    # print(tree)

    r_value = tree[1]
    s_value = tree[N // 2]

    print("#{} {} {}".format(tc, r_value, s_value))