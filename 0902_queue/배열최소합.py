import sys
sys.stdin = open('배열최소합.txt')


def find_min_sum(r, case_sum):
    global min_num

    if case_sum > min_sum: # 지금까지 더한 값(case_sum)이 min_sum보다 크면 더 이상 탐색할 필요 없다.(가지치기)
        return

    if r == N:
        if case_sum < min_sum:
            min_sum = case_sum
        return

    for i in range(N):
        if col[i] == 0: # 해당 열에서 선택할 수 있을 때
            col[i] = 1 # 선택하고
            case_sum += arr[r][i] # 값을 case_sum에 추가하고

            find_min_sum(r+1, case_sum) # 다음 행으로 이동해 다시 함수를 호출한다.

            col[i] = 0 # 함수 호출이 끝나면(선택을 취소하면), 해당 열을 선택할 수 있게 되돌리고
            case_sum -= arr[r][i]  # 값을 case_sum에서 뺀다.

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
