import sys
sys.stdin = open('행렬찾기.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # matrix 순회 하면서 영역 찾고, 찾은 영역은 0으로 변환
    bottles = list()
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                # 영역 시작 >> 약품이 놓인 영역 검사
                # 서브매트릭스 영역 검사 : 0이 나오거나 영익이 끝날때 까지
                row = 0
                col = 0
                for k in range(i, N):
                    if matrix[k][j] == 0:
                        break
                    else:
                        row += 1
                for k in range(j, N):
                    if matrix[i][k] == 0:
                        break
                    else:
                        col += 1
                # 찾을 영역의 내용을 0으로 바꿔준다.
                for l in range(i, i+row):
                    for m in range(j, j+col):
                        matrix[l][m] = 0

                bottles.append((row*col, row, col))
    # print(bottles)
                # 영역검사 끝, 출력
                # 영역이 작은순, 행이 작은순
                # 정렬 > bottles
                for o in range(1, len(bottles)): # 필요한 패스의 개수, 요소가 N개면 N-1번 패스가 필요하다.
                    for p in range(len(bottles)-o): # 각 패스 당 필요한 정렬의 개수
                        if bottles[p][0] > bottles[p+1][0]: # 영역의 크기가 크면 뒤로
                            bottles[p], bottles[p+1] = bottles[p+1], bottles[p]
                        elif bottles[p][0] == bottles[p+1][0]: # 영역의 크기가 같다면
                            if bottles[p][1] > bottles[p+1][1]: # 행 길이 비교
                                bottles[p], bottles[p+1] = bottles[p+1], bottles[p]

    print("#{}".format(tc), end=" ")
    print(len(bottles), end=" ")
    for i in range(len(bottles)):
        print(bottles[i][1], bottles[i][2], end=" ")
    print()

