import sys
sys.stdin = open('Algo1_구미_1반_안세익.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(N, M, K)
    # print(arr)

    max_num = 0
    min_num = 100 * (N * M)

    # 시작점 찾기(도넛모양의 좌측 상단)
    for r in range(N - K + 1):
        for c in range(M - K + 1):
            case_sum = 0
            for i in range(K):
                # 시작점에서 오른쪽으로 사이즈만큼 이동하며 더하기
                case_sum += arr[r][c + i]
                # 시작점에서 아래로 사이즈만큼 이동한 상태에서 오른쪽으로 사이즈만큼 이동하며 더하기기
                case_sum += arr[r + K - 1][c + i]
                # 시작점에서 아래로 사이즈만큼 이동하며 더하기
                case_sum += arr[r + i][c]
                # 시작점에서 오른쪽으로 사이즈만큼 이동한 상태에서 아래쪽으로 사이즈만큼 이동하며 더하기
                case_sum += arr[r + i][c + K - 1]
            # 꼭지점(좌상단, 우상단, 좌하단, 우하단)에 있는 값들은 중복하여 더해졌기 때문에 한번씩 빼준다.
            case_sum -= (arr[r][c] + arr[r][c + K - 1] + arr[r + K - 1][c] + arr[r + K - 1][c + K - 1])
            if case_sum > max_num:
                max_num = case_sum
            if case_sum < min_num:
                min_num = case_sum

    result = max_num - min_num
    print("#{} {}".format(tc, result))