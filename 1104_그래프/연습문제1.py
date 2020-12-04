'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

class Stack():
    def __init__(self, n):
        self.top = -1
        self.s = [0] * n

    def push(self, d):
        if self.top == len(self.s) - 1:
            return False
        self.top += 1
        self.s[self.top] = d

    def pop(self):
        if self.top == -1:
            return False
        value = self.s[self.top]
        self.s[self.top] = 0
        self.top -= 1
        return value


def dfs(v):
    stack = Stack(10)
    stack.push(v)
    print(v, end=" ")
    while sum(stack.s):
        v = stack.s[stack.top]
        visited[v] = 1
        for w in range(1, V + 1):
            if G[v][w] == 1 and visited[w] == 0:
                stack.push(w)
                print(w, end=" ")
                break
        else:
            stack.pop()


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
dfs(1)



