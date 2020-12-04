# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해보자
"""
01D06079861D79F99F
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

# print(binary_arr)

# print(len(binary_arr))

for i in range(0, len(binary_arr), 7):
    tmp = binary_arr[i : i + 7]
    ind = 0
    num = 0
    for i in range(len(tmp) - 1, -1, -1):
        if tmp[i] == 1:
            num += (2 ** ind)
        ind += 1
    print(num, end=" ")



