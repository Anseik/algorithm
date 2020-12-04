import sys
sys.stdin = open('배열최소합.txt')


def find_min_sum(r, case_sum):
    global min_num

    if r == N:
        if case_sum < min_sum:
            min_sum = case_sum
        return

    for i in range(N):
        if not col[i]: # 해당 열에서 선택할 수 있을 때
            col[i] = 1 # 선택하고
            tmp = case_sum + arr[r][i] # 임시변수에 담아서
            if tmp < min_sum: # 지금까지 더한 값이 min_sum보다 작은지 확인하고 작을 때만 탐색 계속
                find_min_sum(r+1, tmp) #
            col[i] = 0 # 함수 호출이 끝나면(선택을 취소하면), 해당 열을 선택할 수 있게 되돌리고

    return # for문이 종료되면 더 이상 선택할 수 있는 열이 없으므로 되돌아 간다.


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(arr)
    col = [0] * N # 해당 열의 선택가능 여부를 확인
    min_num = 9 * N # 이론상 가능한 가장 큰 수로 초기화

    # 함수실행
    find_min_sum(0, 0)

    print("#{} {}".format(tc, min_num))
