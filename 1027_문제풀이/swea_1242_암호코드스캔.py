import sys
sys.stdin = open('swea_1242_암호코드스캔.txt')


code_dict = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}


def solve(line):
    # print(line)
    global idx, ans

    # 시작지점 찾기
    for j in range(idx, -1, -1):
        if line[j] == '0':
            continue
        idx = j
        # 암호코드 시작, 암호의 개수는 총 8개
        pwd = list()
        for k in range(8):
            n1 = n2 = n3 = n4 = 0  # 암호의 각 구성을 세기 위한 변수
            # 0101 순으로 구성되어 있고 뒤에서부터 확인한다.
            cnt = 0
            while line[idx] == '1':
                n4 += 1
                idx -= 1
            while line[idx] == '0':
                n3 += 1
                idx -= 1
            while line[idx] == '1' and idx >= 0:
                n2 += 1
                idx -= 1

            multi = min(n2, n3, n4)

            t2 = n2 // multi
            t3 = n3 // multi
            t4 = n4 // multi
            n1 = (7 - (t2 + t3 + t4)) * multi
            idx -= n1

            pwd.insert(0, code_dict[(t2, t3, t4)])


        # 정상적인 암호인지 검사
        sum_odd = pwd[0] + pwd[2] + pwd[4] + pwd[6]
        sum_even = pwd[1] + pwd[3] + pwd[5]
        test = pwd[7]
        tmp = (sum_odd * 3) + sum_even + test
        if tmp % 10 == 0:
            if not pwd in result:
                ans += sum(pwd)
        return


hex_dict = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    check = []
    for r in range(N):
        cnt = 0
        for c in range(M):
            if board[r][c] != '0':
                cnt += 1

                # 세로로 반복되는 암호코드를 '0'으로 바꾼다.
                row = r + 1
                while True:
                    if board[row][c] != '0':
                        board[row][c] = '0'
                        row += 1
                    else:
                        break

        if cnt: # 암호코드가 들어있는 열이면
            check.append(board[r])


    result = []
    ans = 0
    for code in check:
        line = ''
        for i in range(len(code)):
            line += hex_dict[code[i]]
        line = line.strip('0')
        idx = len(line) - 1
        # print(line)
        while idx >= 0:
            solve(line)
            # 같은 줄에 다음 암호코드 탐색을 위한 슬라이싱 및 '0'제거
            if idx >= 0 :
                line = line[:idx + 1].strip('0')
                idx = len(line) - 1

    print('#{} {}'.format(tc, ans))