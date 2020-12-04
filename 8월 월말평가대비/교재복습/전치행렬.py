arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for r in range(len(arr)):
    for c in range(r+1, len(arr[r])):
        arr[r][c], arr[c][r] = arr[c][r], arr[r][c]

print(arr)

