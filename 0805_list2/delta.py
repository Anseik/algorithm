# delta : 원하는 순서대로 2차원 배열을 순회하기 위해서 사용
# 상하좌우 순서로 접근할 수 있는 델타
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
#     상  하  좌  우

#     c0    c1    c2
# r0 [0,0] [0,1] [0,2]
# r1 [1,0] [1,1] [1,2]
# r2 [2,0] [2,1] [2,2]

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
      ]
r = 1
c = 1
# print(arr[r][c])
# r += dr[2]
# c += dc[2]
# print(arr[r][c])
# 상하좌우 연속으로 순회하기
sum_v = 0
for i in range(8):
    # 다음 좌표를 계산
    nr = r + dr[i]
    nc = c + dc[i]
    sum_v += arr[nr][nc]
print(sum_v)