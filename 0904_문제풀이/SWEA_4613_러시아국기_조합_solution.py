# 조합구하기
# selected : 요소 선택 표시
# idx : 요소를 가리키기 위한 인덱스
# cnt : 선택된 요소의 개수를 세기위한 변수


import sys
sys.stdin = open('SWEA_4613_러시아국기.txt')


def comb(selected, idx, cnt):
    # 마지막행을 제외한 모든행을 선택하면, 재귀 종료
    # 세개의 영역을 구분해서 색깔을 바꿔야할 칸 수 세기
    global min_cnt

    if cnt == 2:

        i, j = -1, -1
        for k in range(N):
            if selected[k] == 1:
                if i == -1:
                    i = k
                else:
                    j = k

        cnt = 0
        # 흰색 영역 순회하면서 바꿔야할 개수 세기
        for w in range(0, i + 1):
            for k in range(M):
                if flag[w][k] != "W":
                    cnt += 1
        # 파란 영역 순회하면서 바꿔야할 개수 세기
        for b in range(i + 1, j + 1):
            for k in range(M):
                if flag[b][k] != "B":
                    cnt += 1
        # 빨간 영역 순회하면서 바꿔야할 개수 세기
        for r in range(j + 1, N):
            for k in range(M):
                if flag[r][k] != "R":
                    cnt += 1

        # cnt가 가장 작으면 min_cnt에 저장
        if cnt < min_cnt:
            min_cnt = cnt

        return

    if idx == N - 1:
        return

    selected[idx] = 1
    comb(selected, idx + 1, cnt + 1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    min_cnt = 2500
    selected = [0] * N
    comb(selected, 0, 0)
    print("#{} {}".format(tc, min_cnt))