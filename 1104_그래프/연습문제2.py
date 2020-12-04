'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


class Queue:
    def __init__(self, n):
        self.q = [0] * n
        self.front = -1
        self.rear = -1

    def enQueue(self, d):
        self.rear += 1
        self.q[self.rear] = d

    def deQueue(self):
        self.front += 1
        value = self.q[self.front]
        self.q[self.front] = 0
        return value


def bfs(v):
    Q = Queue(10)
    Q.enQueue(v)
    visited[v] = 1
    while sum(Q.q):
        v = Q.deQueue()
        print(v, end = " ")
        for w in range(1, V + 1):
            if G[v][w] == 1 and not visited[w]:
                Q.enQueue(w)
                visited[w] = 1


V, E = map(int, input().split())
G = [[0] * (V + 1) for _ in range(V + 1)]
# print(G)
tmp = list(map(int, input().split()))
# print(tmp)
for i in range(E):
    s, e = tmp[2 * i], tmp[2 * i + 1]
    G[s][e] = 1
    G[e][s] = 1
# print(G)

visited = [0] * (V + 1)
bfs(1)
