import sys
sys.stdin = open('Algo1_구미_1반_안세익.txt')

T = int(input())
for tc in range(1, T+1):
    # N : 배열의 크기
    # M : 첫 번째 입력 값
    # D : 변경 값
    N, M, D = map(int, input().split())
    # print(tc, N, M, D)

    arr = [[0] * N for _ in range(N)] # 배열 초기화
    # print(arr)

    s = (N-1) // 2 # 중앙점(시작점)
    n = (N+1) // 2 # 반복문을 돌아야 하는 횟수
    tmp = M - D # 반복조건을 만족하기 임시 변수 ex) 첫번째 tc에서 tmp가 3으로 시작해야 시작점에 5가 채워진다.

    # 반복문 돌면서 빈곳 채워 나가기
    for i in range(n): # 동심원을 채워나가는 첫번째 패스 ~ n번째 패스
        tmp += D # 패스를 돌때마다 값의 변화량을 더 해준다.(변화량이 음수이면 빼진다)
        for j in range(s-i, s-i-1, -1): # 동심원을 채워나가는 좌측 상단 시작점(s-i), for문을 한번만 돌면된다.
            for r in range(j, j + 2 * i + 1): # 채워나가야 하는 영역의 행 길
                for c in range(j, j + 2 * i + 1): # 채워나가야 하는 영역의 열
                    if arr[r][c] == 0: # 안쪽부터 채워져 나오고 있기때문에 해당 칸이 0일때만 채운다.
                        arr[r][c] = tmp

    print("#{}".format(tc), end=" ")
    for row in arr:
        print(sum(row), end=" ")
    print()





