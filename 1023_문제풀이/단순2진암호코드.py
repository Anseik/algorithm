import sys
sys.stdin = open('단순2진암호코드.txt')

def check(codes):
    test = codes[-1]
    tmp = 0
    for m in range(len(codes) - 1):
        if not m % 2:  # 홀수번째 자리(인덱스로 보면 짝수)
            tmp += (codes[m] * 3)
        else:
            tmp += codes[m]

    result = 0
    if not (tmp + test) % 10: # 10의 배수이면
        result = sum(codes)

    return result


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # print(N, M)
    # print(arr)

    dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    ans = 0
    for r in range(N):
        line_sum = 0
        for c in range(M):
            line_sum += int(arr[r][c])
        if line_sum == 0:
            continue # 줄의 합이 0이면 그곳에는 암호코드가 없으므로 넘어간다.

        for s in range(M - 55): # 암호코드 시작이 어디인지 알 수 없으므로 가능한 모든 시작점을 검사한다.
            codes = []
            for j in range(8): # 한줄을 7개씩 8번 슬라이싱한다.
                key = arr[r][s + (7 * j) : s + (7 * (j + 1))]
                if key in dict.keys(): # 슬라이싱한 문자열을 키로가지는 값을 codes에 append한다.
                    codes.append(dict[key])
                else: # 슬라이싱한 문자열이 키가 아니면 다음 시작점을 검사한다.
                    break
            # print(codes)

            else: # break되지 않고 슬라이싱이 완료되면
                result = check(codes) # 정상적인 암호코드인지 확인한다.
                if result: # 정상적인 암호코드라면(리턴 값이 0이 아니면)
                    ans = result # 리턴 값을 답으로하고 for문을 break한다.
                    break
        break # 암호코드가 있는 한 줄만 검사하면 되므로 break한다.

    print('#{} {}'.format(tc, ans))


