import sys
sys.stdin = open('swea_5247_연산_solution.txt')

def calc(num, idx):
    if idx == 0:
        return num + 1
    elif idx == 1:
        return num - 1
    elif idx == 2:
        return num * 2
    else:
        return num - 10

def bfs():
    queue = [0] * 1000000
    front = rear = -1
    rear += 1
    queue[rear] = (N, 0) #(숫자, 연산횟수)
    memo[N] = 0
    while front != rear:
        front += 1
        curr_n, curr_cnt = queue[front]

        if curr_n == M:
            return curr_cnt
        for i in range(4):
            next_n = calc(curr_n, i)
            if 0 < next_n <= 1000000 and memo[next_n] == -1:
                rear += 1
                queue[rear] = (next_n, curr_cnt + 1)
                memo[next_n] = memo[curr_n] + 1




from collections import deque

def bfs2():
    queue = deque()
    queue.append(N)
    ans = 0

    while queue:
        size = len(queue) # 현재 레벨의 요소 수
        for i in range(size):
            curr = queue.popleft()
            if curr == M:
                return ans

            for j in (curr + 1, curr - 1, curr * 2, curr - 10):
                if 0 < j <= 1000000 and memo[j] == -1:
                    memo[j] = 1
                    queue.append(j)
        ans += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    memo = [-1] * 1000001

    result = bfs2()
    print('#{} {}'.format(tc, result))

