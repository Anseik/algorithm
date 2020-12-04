# 16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오 암호는 연속되어 있다.

# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해보자
"""
0269FAC9A0
"""
hex_dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

hex_arr = input()
binary_arr = []
for i in range(len(hex_arr)):
    if hex_arr[i] in hex_dict:
        target = hex_dict[hex_arr[i]]
    else:
        target = int(hex_arr[i])
    bi_list = [0, 0, 0, 0]
    ind = 3
    while target >= 1:
        bi_list[ind] = target % 2
        target //= 2
        ind -= 1
    binary_arr.extend(bi_list)

binary_str = list(map(str, binary_arr))
codes = ''.join(binary_str)
# print(len(codes))

secret = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}

for s in range(len(codes)): # 시작점을 증가시켜 가면서
    key = codes[s : s + 6]
    if key in secret:
        for i in range(s, len(codes), 6):
            sec = codes[i : i + 6]
            if len(sec) == 6:
                print(secret[sec], end=" ")
        break








