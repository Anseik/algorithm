import sys
sys.stdin = open('swea_1242_암호코드스캔.txt')


code_dict = {
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


def solve(arr):
    global idx
    # print(idx)
    for j in range(idx, -1, -1):  # 열을 뒤쪽부터 검사
        if arr[j] == 0:  # 암호코드 시작 아님
            continue

        # 암호코드 시작, 암호의 개수는 총 8개
        idx = j  # 시작 인덱스
        # print(idx)
        pwd = list()
        size = 0
        for k in range(8):
            n1 = n2 = n3 = n4 = 0  # 암호의 각 구성을 세기 위한 변수
            # 0101 순으로 구성되어 있고 뒤에서부터 확인한다.
            cnt = 0
            while arr[idx] == 1:
                n4 += 1
                cnt += 1
                arr[idx] = 0
                idx -= 1
            while arr[idx] == 0:
                n3 += 1
                cnt += 1
                arr[idx] = 0
                idx -= 1
            while arr[idx] == 1:
                n2 += 1
                cnt += 1
                arr[idx] = 0
                idx -= 1
            while arr[idx] == 0:
                n1 += 1
                cnt += 1
                arr[idx] = 0
                idx -= 1
                if k == 7 and cnt == size:
                    break
            if k == 0:
                size = cnt

            # print(cnt)
            # print(n1, n2, n3, n4)
            d = cnt // 7
            # print(d)
            n1 //= d
            n2 //= d
            n3 //= d
            n4 //= d
            pwd.insert(0, code_dict[(n1, n2, n3, n4)])


        # 정상적인 암호인지 검사
        sum_odd = pwd[0] + pwd[2] + pwd[4] + pwd[6]
        sum_even = pwd[1] + pwd[3] + pwd[5]
        test = pwd[7]
        tmp = (sum_odd * 3) + sum_even + test
        if tmp % 10 == 0:
            if not pwd in result:
                result.append(pwd)
            return
        else:
            return


def hex_to_decimal(c):
    num = ord(c)
    if 48 <= num <= 57:
        return num - 48
    elif 65 <= num <= 70:
        return num - ord('A') + 10


def decimal_to_binary(n): # 0 ~ 15
    binary = [0] * 4 # 0 ~ 15까지는 4개의 비트로 처리가능
    idx = 3
    while n > 0:
        # n을 2로 나누어서 나머지를 계속 저장
        binary[idx] = n % 2
        idx -= 1
        n = n // 2
    return binary


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    # print(N, M)
    # print(board)



    # 배열에서 나오는 패턴을 찾는다.
    ptns = set()

    check = []
    for r in range(N):
        cnt = 0
        for c in range(M):
            if board[r][c] != '0':
                cnt += 1
        if cnt: # 암호코드가 들어있는 열이면
            tmp = ''.join(board[r])
            if tmp in check:
                pass
            else:
                check.append(tmp)
    # print(check)

    result = []
    for code in check:
        # print(code)
        arr = []
        for i in range(len(code)):
            c = code[i]
            n = hex_to_decimal(c)
            binary = decimal_to_binary(n)
            arr.extend(binary)
        # print(arr)
        idx = len(arr) - 1
        while sum(arr):
            solve(arr)

    # print(result)
    ans = 0
    for k in range(len(result)):
        ans += sum(result[k])

    print('#{} {}'.format(tc, ans))



