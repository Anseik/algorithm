'''
7
4 50
2 160
3 30
1 60
3 20
1 100

7
1 100
4 50
2 160
3 30
1 60
3 20

1
2 50
3 100
1 200
4 60
2 150
4 40
'''
K = int(input())
# 큰 사각형에서 작은 사각형(사각 형에서 제외되는 영역)을 빼면 참외밭의 넓이를 알 수 있다.

# 큰 사각형의 변의 길이를 구한다.
row_max = 0
col_max = 0
info_list = []
for i in range(6):
    dir, length = map(int, input().split())
    info_list.append((dir, length))
    if dir == 1 or dir == 2: # 가로방향
        if length > row_max:
            row_max = length
    else: # 세로방향
        if length > col_max:
            col_max = length
# print(row_max, col_max)
# print(info_list)

# 작은 사각형의 변의 길이를 구한다. 1, 3, 1, 3처럼 반복되는 패턴이 나오면 중간에 있는 3, 1이 작은사각형의 변의 길이다.
min1 = 0
min2 = 0
# 리스트를 회전시키며 반복되는 패턴을 찾는다.
while True:
    if info_list[0][0] == info_list[2][0]:
        min1 = info_list[1][1]
        min2 = info_list[2][1]
        break
    else:
        info_list.append(info_list.pop(0))
# print(min1, min2)

big_square = row_max * col_max
small_square = min1 * min2
area = big_square - small_square
result = area * K
print(result)

