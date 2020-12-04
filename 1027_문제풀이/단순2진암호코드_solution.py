import sys
sys.stdin = open('단순2진암호코드.txt')

code = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}

# board에서 암호코드를 읽어서 반환
# 암호코드의 합 또는 0을 반환
def solve():
    # 열의 뒤쪽 부터 검사 시작 : 모든 암호의 끝은 1로 끝이남.
    # 부분만 있는 암호가 없기때문에 1을 찾으면 연속된 8개의 숫자를 찾을 수 있다.
    for i in range(N):
        for j in range(M - 1, -1, -1):  # 열을 뒤쪽부터 검사
            if board[i][j] == '0':  # 암호코드 시작 아님
                continue

            # 암호코드 시작, 암호의 개수는 총 8개
            idx = j  # 시작 인덱스
            pwd = list()
            for k in range(8):
                n1 = n2 = n3 = n4 = 0  # 암호의 각 구성을 세기 위한 변수
                # 0101 순
                while board[i][idx] == '1':
                    n4 += 1
                    idx -= 1
                while board[i][idx] == '0':
                    n3 += 1
                    idx -= 1
                while board[i][idx] == '1':
                    n2 += 1
                    idx -= 1
                n1 = 7 - (n2 + n3 + n4)
                idx -= n1
                pwd.insert(0, code[(n1, n2, n3, n4)])

            # 정상적인 암호인지 검사
            #
            sum_odd = pwd[0] + pwd[2] + pwd[4] + pwd[6]
            sum_even = pwd[1] + pwd[3] + pwd[5]
            test = pwd[7]
            tmp = (sum_odd * 3) + sum_even + test
            if tmp % 10 == 0:
                return (sum_odd + sum_even + test)
            else:
                return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    result = solve()
    print('#{} {}'.format(tc, result))


