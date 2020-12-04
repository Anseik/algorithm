arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = 3

def turn_90(arr):
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = arr[r][c]

    return ret

result = turn_90(arr)
print(result)