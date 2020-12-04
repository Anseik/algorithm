import sys
from collections import deque
sys.stdin = open('boj_9019_DSLR.txt')

def solve():
    def D(n):
        return 2 * n % 10000

    def S(n):
        return (n - 1) % 10000

    def L(n): # 1234
        return n * 10 % 10000 + (n // 1000)

    def R(n): # 1234
        return 1000 * (n % 10) + n // 10

    A, B = map(int, input().split())

    visited = [None] * 10000
    visited[A] = A

    K = [None] * 10000

    q = deque([A])

    while q:
        cur = q.popleft()

        if cur == B:
            break

        for order in (D, S, L, R):
            n = order(cur)
            if visited[n] is None:
                visited[n] = cur
                K[n] = order.__name__
                q.append(n)

    result = []

    t = B

    while visited[t] != t:
        result.append(K[t])
        t = visited[t]

    print(''.join(result[::-1]))


T = int(input())
for tc in range(1, T + 1):
    solve()

