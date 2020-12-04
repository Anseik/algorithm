'''
7
4 50
2 160
3 30
1 60
3 20
1 100
'''
K = int(input())
# 큰 사각형에서 작은 사각형(사각 형에서 제외되는 영역)을 빼면 참외밭의 넓이를 알 수 있다.
row_max = 0
row_min = 500
col_max = 0
col_min = 500
for i in range(6):
    dir, length = map(int, input().split())
    if dir == 1 or dir == 2: # 가로방향
        if length > row_max:
            row_max = length
        if length < row_min:
            row_min = length
    else: # 세로방향
        if length > col_max:
            col_max = length
        if length < col_min:
            col_min = length

big_area = row_max * col_max
small_area = row_min * col_min
area = big_area - small_area
result = area * K
print(result)

