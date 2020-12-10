def solve(idx):
    if idx == N:
        print(*result)
        return

    for i in range(1, 7):
        result[idx] = i
        solve(idx + 1)
        result[idx] = 0


N = 3
result = [0] * N
solve(0)
