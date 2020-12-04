import sys
sys.stdin = open('swea_5185_이진수.txt')

hex_dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

# 10진수를 2진수로 변환하는 함수
def decimal_to_binary(num):
    # 0 ~ 15까지를 2진수로 변환
    bi_list = [0] * 4
    target = num
    idx = 3
    while target > 0:
        rest = target % 2
        bi_list[idx] = rest
        target //= 2
        idx -= 1

    result.extend(bi_list)


T = int(input())
for tc in range(1, T + 1):
    N, hex = input().split()
    N = int(N)

    result = []
    for i in range(N):
        # 문자로된 16진수 일때 10진수 변환
        if hex[i] in hex_dict:
            num = hex_dict[hex[i]]
        # 숫자 16진수 일때 10진수 변환
        else:
            num = int(hex[i])
        decimal_to_binary(num)

    ans = ''.join(list(map(str, result)))
    print('#{} {}'.format(tc, ans))
