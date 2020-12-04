# 방법1 반복문으로 풀기
# 최소 파란색과 빨간색이 한 칸 씩은 있어야 한다.
# W : 0 ~ N - 2 - 1
# for w in range(0, N - 2)
# B : W + 1 ~ N - 1 - 1
# for b in range(w + 1, N - 1)
# R : B + 1 ~ N
# for r in range(b + 1, N)

# 전체 중에 2개의 행을 선택하면 전체를 세 부분으로 나눌 수 있음
# 흰색 영역이 끝나는 행(흰색에 포함)
# 파란 영역이 끝나는 행(파란색에 포함)
import sys
sys.stdin = open('SWEA_4613_러시아국기.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    # print(N, M)
    # print(flag)

    min_color = float('inf') # 새로 칠해야 하는 칸의 개수의 최소값
    w_color_list = []
    b_color_list = []
    r_color_list = []
    for w in range(0, N - 2): # 흰색영역이 끝나는행
        w_color = 0 # 흰색으로 색칠해야하는 칸의 수
        for i in range(0, w + 1):
            for j in range(M):
                if flag[i][j] != "W":
                    w_color += 1
        w_color_list.append(w_color)


        for b in range(w + 1, N - 1): # 파란색 영역이 끝나는 행
            b_color = 0  # 파란색으로 색칠해야하는 칸의 수
            for i in range(w + 1, b + 1):
                for j in range(M):
                    if flag[i][j] != "B":
                        b_color += 1
            b_color_list.append(b_color)


            r_color = 0  # 빨간색으로 색칠해야하는 칸의 수
            for i in range(b + 1, N):
                for j in range(M):
                    if flag[i][j] != "R":
                        r_color += 1
            r_color_list.append(r_color)

    print(w_color_list)
    print(b_color_list)
    print(r_color_list)



