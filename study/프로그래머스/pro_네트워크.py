def solution(n, computers):
    answer = 0
    visit = [0] * n
    def dfs(v):
        visit[v] = 1
        for w in range(n):
            if computers[v][w] and not visit[w]:
                dfs(w)

    for v in range(n):
        if not visit[v]:
            answer += 1
            dfs(v)

    return answer


n1 = 3
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n2 = 3
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
result1 = solution(n1, computers1)
result2 = solution(n2, computers2)
print(result1)
print(result2)