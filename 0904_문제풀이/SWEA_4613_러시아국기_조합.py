import sys
sys.stdin = open('SWEA_4613_러시아국기.txt')


def comb(selected, idx, cnt):
    # idx가 범위를 벗어나거나, 원하는 만큼의 요소를 이미 선택했을 때 더이상 진행 안함
    if cnt == 2: # 필요한 개수만큼 선택함
        pos = []
        for i in range(N - 1):
            if selected[i] == 1:
                pos.append(arr[i])
        line.append(pos)

        return

    if idx == N - 1: # 범위 벗어남
        return

    # 요소의 포함/미포함 여부 결정
    selected[idx] = 1
    comb(selected, idx + 1, cnt + 1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    # print(N, M)
    # print(flag)
    arr = [i for i in range(N - 1)]
    # print(arr)

    selected = [0] * (N - 1)
    # print(selected)

    line = []
    comb(selected, 0, 0)
    # print(line)


    min_cnt = float('inf') # 새로 칠해야 하는 칸의 개수의 최소값
    for i in range(len(line)):
        a, b = line[i][0], line[i][1]
        cnt = 0
        # 흰색 영역 순회하면서 바꿔야할 개수 세기
        for w in range(0, a+1):
            for k in range(M):
                if flag[w][k] != "W":
                    cnt += 1
        # 파란 영역 순회하면서 바꿔야할 개수 세기
        for b in range(a+1, b+1):
            for k in range(M):
                if flag[b][k] != "B":
                    cnt += 1
        # 빨간 영역 순회하면서 바꿔야할 개수 세기
        for r in range(b+1, N):
            for k in range(M):
                if flag[r][k] != "R":
                    cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt

    print("#{} {}".format(tc, min_cnt))



