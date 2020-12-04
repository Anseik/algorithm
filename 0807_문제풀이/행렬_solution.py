import sys
sys.stdin = open('행렬.txt')
#행렬 접근하기
# 1 2 0 0 0 1
# 2 1 0 0 0 0
# 0 0 1 2 3 2
# 0 0 3 2 1 3
# 0 0 2 1 3 4
# 0 0 0 0 0 0
# 위 행렬을 입력받아서
# 행렬에 포함되어 있는 sub matrix 크기 계산하기
T = int(input())
for tc in range(1,T+1): # range가 빠졌음
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    #할일
    # matrix 순회하면서 0이 아닌 위치 찾기
    # 가로, 세로 길이 구해서 저장
    # 표시한 영역은 0으로 다 바꾸기
    area = []
    for i in range(n): # 전체 세로
        for j in range(n): # 전체 가로
            if matrix[i][j] != 0:
                #가로, 세로 길이 구하기
                x = 0 #가로길이(열의 길이)
                for k in range(j,n):
                    if matrix[i][k]:
                        x += 1
                    else:
                        break
                y = 0 # 세로길이(행의 길이)
                for k in range(i,n):
                    if matrix[k][j]:
                        y += 1
                    else:
                        break
                # 표시한 영역은 0으로 다 바꾸기
                for k in range(i,i+y):
                    for l in range(j,j+x):
                        matrix[k][l] = 0

                area.append([y, x, x*y])  # y가 행이고 x가 열이므로 y, x 순서로 넣어야 함
    #tuple (y,x,y*x)

    # print(area)
    for i in range(len(area)):
        min = i
        for j in range(i+1,len(area)):
            if area[min][2] > area[j][2]:
                min = j
            elif area[min][2] == area[j][2] and area[min][0] > area[min][0]:
                min = j
        area[min], area[i] = area[i], area[min]

    # print(area)

    print('#%d' %tc, len(area), end=' ')
    for i in range(len(area)):
        for j in range(2):
            print(area[i][j], end =' ')
    print()



