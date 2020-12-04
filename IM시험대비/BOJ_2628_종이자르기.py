import sys
sys.stdin = open('BOJ_2628_종이자르기.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    global area
    area += 1
    paper[r][c] = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < len(paper) and 0 <= nc < len(paper[0]) and paper[nr][nc] == 1:
            dfs(nr, nc)


width, height = map(int, input().split())
# print(width, height)
paper = [[1] * (width) for _ in range(height)]
# print(paper)
N = int(input())

for i in range(N):
    direction, cut = map(int, input().split())
    # print(direction, cut)

    # 가로로 자를 때
    if direction == 0:
        line = [0] * (len(paper[0]))
        paper.insert(cut, line)
    # 세로로 자를 때
    else:
        for j in range(len(paper)):
            paper[j].insert(cut, 0)

# print(paper)
max_area = 0
for r in range(len(paper)):
    for c in range(len(paper[0])):
        if paper[r][c] == 1:
            area = 0
            dfs(r, c)
            if area > max_area:
                max_area = area

print(max_area)