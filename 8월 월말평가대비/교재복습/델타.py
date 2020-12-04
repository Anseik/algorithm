arr = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15],
       [16,17,18,19,20],
       [21,22,23,24,25]
       ]
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

sum = 0
for r in range(len(arr)):
    for c in range(len(arr[r])):
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < len(arr) and 0 <= nc < len(arr[r]):
                sum += abs(arr[nr][nc] - arr[r][c])


print(sum)
