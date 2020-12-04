import sys
sys.stdin = open('sum.txt')

T = 10
for tc in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    N = len(arr)  # 행의 길이
    M = len(arr[0])  # 열의 길이

    max_num = 0 # 최대 값을 비교하기 위한 변수 선언
    total_dia1 = 0
    total_dia2 = 0
    #가로
    for row in range(N):
        total_row = 0 # 열이 바뀔때 마다 0으로 초기화 해야하므로 위치 조정
        for rowin in range(M):
            total_row += arr[row][rowin]
            if row == rowin: #왼오대각선
                total_dia1 += arr[row][rowin]
            elif row + rowin == len(arr)-1: #오왼 대각선
                total_dia2 += arr[row][rowin] # [행][열] 순으로 조정 [row][rowin]

        if total_row > max_num: # 각 행을 순회할때 마다 total_row와 max_sum을 비교하여 total_row가 더 크면 max_sum에 저장
            max_num = total_row
    if total_dia1 > max_num: # for 문을 다 돌고 나야 대각선의 합이 구해지므로 for문 밖에서 if 문으로 비교하여 값이 더 크면 max_sum에 저장
        max_num = total_dia1
    if total_dia2 > max_num:
        max_num = total_dia2


    for col in range(M): # 열 우선 순회
        total_col = 0
        for colin in range(N):
            total_col += arr[colin][col]

        if total_col > max_num: # 각 열의 합이 max_sum보다 큰지 비교하고 크면 max_sum에 저장
            max_num = total_col

    print('#%d' % tc, max_num)