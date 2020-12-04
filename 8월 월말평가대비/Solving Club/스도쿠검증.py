import sys
sys.stdin = open("스도쿠검증.txt")

def check_sudoku(sudoku):
    for r in range(N):
        row_check = [0] * (N + 1)
        col_check = [0] * (N + 1)
        for c in range(N):
            row_check[sudoku[r][c]] += 1
            col_check[sudoku[c][r]] += 1
            if row_check[sudoku[r][c]] > 1 or col_check[sudoku[c][r]] > 1:
                return 0

            if r % 3 == 0 and c % 3 == 0:
                area_check = [0] * (N + 1)
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        area_check[sudoku[i][j]] += 1
                        if area_check[sudoku[i][j]] > 1:
                            return 0

    return 1

T = int(input())
N = 9
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(N)]
    # print(sudoku)
    result = check_sudoku(sudoku)
    print("#{} {}".format(tc, result))



