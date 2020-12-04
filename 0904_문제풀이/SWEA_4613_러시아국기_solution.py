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

    min_cnt = float('inf') # 새로 칠해야 하는 칸의 개수의 최소값
    for i in range(0, N - 2): # 흰색영역이 끝나는행
        for j in range(i + 1, N - 1): # 파란색 영역이 끝나는 행
            # 여기서 세개의 영역으로 구분할 수 있음
            # 0 ~ i, i+1 ~ j, j+1 ~ 끝
            cnt = 0
            # 흰색 영역 순회하면서 바꿔야할 개수 세기
            for w in range(0, i+1):
                for k in range(M):
                    if flag[w][k] != "W":
                        cnt += 1
            # 파란 영역 순회하면서 바꿔야할 개수 세기
            for b in range(i+1, j+1):
                for k in range(M):
                    if flag[b][k] != "B":
                        cnt += 1
            # 빨간 영역 순회하면서 바꿔야할 개수 세기
            for r in range(j+1, N):
                for k in range(M):
                    if flag[r][k] != "R":
                        cnt += 1
            if cnt < min_cnt:
                min_cnt = cnt

    print("#{} {}".format(tc, min_cnt))



