import sys
sys.stdin = open('swea_1242_암호코드스캔_solution.txt')

hex_dic = {
    "0": [0, 0, 0, 0], "1": [0, 0, 0, 1], "2": [0, 0, 1, 0], "3": [0, 0, 1, 1],
    "4": [0, 1, 0, 0], "5": [0, 1, 0, 1], "6": [0, 1, 1, 0], "7": [0, 1, 1, 1],
    "8": [1, 0, 0, 0], "9": [1, 0, 0, 1], "A": [1, 0, 1, 0], "B": [1, 0, 1, 1],
    "C": [1, 1, 0, 0], "D": [1, 1, 0, 1], "E": [1, 1, 1, 0], "F": [1, 1, 1, 1]
}

code = {
    (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2,
    (4, 1, 1): 3, (1, 3, 2): 4, (2, 3, 1): 5,
    (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9
}

def solve():
    result = 0

    for i in range(N):
        # 뒤쪽에서부터 검사
        j = M * 4 - 1
        while j >= 55:
            # 만약에 1을 찾았는데 위쪽도 같이 1이면, 암호 첫번째 줄이 아님
            # 검사를 할 필요가 없음
            # 위쪽이 0인줄만 암호코드 해독
            if arr[i][j] == 1 and arr[i-1][j] == 0:
                # 암호코드 해독 시작
                # 암호코드 하나는 8개의 숫자로 이루어져 있음
                pwd = list()
                for _ in range(8):
                    n2 = n3 = n4 = 0
                    while arr[i][j] == 0: # 이전 숫자에서 남아있는 0을 뛰어넘는다.
                        j -= 1
                    while arr[i][j] == 1:
                        n4 += 1
                        j -= 1
                    while arr[i][j] == 0:
                        n3 += 1
                        j -= 1
                    while arr[i][j] == 1:
                        n2 += 1
                        j -= 1
                    min_v = min(n2, n3, n4)
                    c = (n2//min_v, n3//min_v, n4//min_v)
                    pwd.insert(0, code[c])


                sum_odd = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                sum_even = pwd[1] + pwd[3] + pwd[5]
                test = pwd[7]
                tmp = (sum_odd * 3) + sum_even + test
                if tmp % 10 == 0:
                    result += (sum_odd + sum_even + test)

            j -= 1 # 다음 암호코드를 검사하기 위해서 인덱스를 줄여준다.

    return result

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 입력 받기전에... 2진수 형태의 배열이 필요
    # 입력받으면서 2진수로 받아서 받으면 어떨까? --> 2진수로 변환할 수 있는 딕셔너리를 생성하자
    arr = list()
    for i in range(N):
        tmp_arr = list()
        tmp = input()
        for j in range(M):
            tmp_arr += hex_dic[tmp[j]]
        arr.append(tmp_arr)
    result = solve()
    print('#{} {}'.format(tc, result))

