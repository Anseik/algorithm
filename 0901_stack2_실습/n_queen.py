N = 10
# 보드에 놓인 퀸이 영향을 미치는 곳을 표시하기 위한 배열
check = [[0] * N for _ in range(N)]
cnt = 0


def marking(r, c, num): # r,c에 놓여진 퀸에 의해 영향받는 칸에 num(1 or -1)을 더해주는 함수
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for d in range(8):
        nr = r
        nc = c
        while True:
            nr += dr[d]
            nc += dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                break
            check[nr][nc] += num


def n_queen(r):
    global cnt
    if r >= N:
        cnt += 1
        return
    # 각행에서 어느 칸에 퀸이 놓여질지 검사
    # 그 행에서 퀸이 놓일 자리가 결정되면 다음행으로 진행
    # 만약에 마지막 행까지 퀸을 놓게되면, 모든행에 퀸을 놓은 것
    # N개의 퀸을 놓은 것이기 때문에 해를 찾은 것이 된다.
    for i in range(N): # 어떤 칼럼에 퀸을 놓을지 검사
        if check[r][i] == 0: # 표시가 안된 자리는 퀸을 놓을 수 있다.
            # 만약에 현재 칸에 퀸을 놓을 수 있으면 퀸을 놓고
            # r, i에 퀸을 놓고 그 퀸에 영향 받는 칸에 표시(+1)
            # 다음 행으로 진행
            marking(r, i, 1)
            n_queen(r+1)
            # r, i에 놓인 퀸에 의해 표시되었던 칸을 되돌림(-1)
            marking(r, i, -1)
    # 반복문이 끝나면 더 이상 검사할 대상이 없기 때문에 종료
    return

n_queen(0)
print(cnt)
