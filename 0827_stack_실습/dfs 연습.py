# dfs연습하기
# 0 0 0 0 0 0
# 0 0 0 1 1 1
# 0 0 1 0 1 1
# 0 1 1 0 1 0
# 0 0 1 1 1 0
# 0 0 0 0 0 0
N = 6
arr = [list(map(int, input().split())) for _ in range(N)]

# for row in arr:
#     print(row)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

visited = [[0] * N for _ in range(N)]

result = 0
is_find = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0 # 연결된 개수 세기 위한 변수
            # dfs 시작 : 반복문 > stack
            stack = list()
            stack.append((i, j))
            # arr[i][j] = 0
            visited[i][j] = 1
            while stack: # 스택에 요소가 있으면 계속 반복
                # 해당 요소에서 갈 수 있는 길을 모두 검색
                # 갈 수 있는 길이 나오면 stack에 추가, 추가했음을 표시
                cr, cc = stack.pop() # 현재 노드
                cnt += 1
                # 현재 노드에서 갈 수 있는 길을 탐색
                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    # and not visited[nr][nc]
                    if 0 <= nr < len(arr) and 0 <= nc < len(arr) and not visited[nr][nc]:
                        if arr[nr][nc] == 1:
                        # nr, nc 범위내에 있고, 한번도 방문하지 않았으면 방문
                            stack.append((nr,nc))
                            visited[nr][nc] = 1
                            # arr[nr][nc] = 0

            result = cnt
            if cnt > 1:
                is_find = True
        if is_find:
            break
    if is_find:
        break


print(result)

