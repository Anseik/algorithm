import sys
sys.stdin = open('스도쿠.txt')

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # print(sudoku)

    # 0을 무시하고 인덱스와 값을 일치시키기 위해 N+1의 길이로 count를 만든다.
    count_total = [0] * 10 # 해당 tc 전체에서 중복되는 값이 있었는지 확인하기 위한 count

    # 행순회 열순회
    for r in range(len(sudoku)):
        # 각 행 및 열에서 중복여부를 확인하기 위한 count
        count_row = [0] * 10
        count_col = [0] * 10
        for c in range(len(sudoku)):
            count_row[sudoku[r][c]] += 1
            count_col[sudoku[c][r]] += 1

        for over in range(len(count_total)):
            if count_row[over] > count_total[over]:
                count_total[over] = count_row[over]

            if count_col[over] > count_total[over]:
                count_total[over] = count_col[over]

    # print(count_total)

    # 좌상단 좌표를 가지고 3 * 3순회
    start_point = [0, 3, 6]
    for x in start_point:
        for y in start_point:
            count_in = [0] * 10 # 카운팅 정렬을 이용해 중복되는 값이 있는지 체크
            for m in range(3):
                for n in range(3):
                    count_in[sudoku[x+m][y+n]] += 1

            for over in range(len(count_total)):
                if count_in[over] > count_total[over]:
                    count_total[over] = count_in[over]

    result = 1
    for i in range(len(count_total)):
        if count_total[i] > 1:
            result = 0
            break

    print('#%d' %tc, result)