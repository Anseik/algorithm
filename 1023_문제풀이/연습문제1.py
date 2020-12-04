# 이진수 문자열을 입력받아서 7bit마다 10진수 숫자로 변경하라
"""
0000000111100000011000000111100110000110000111100111100111111001100111
"""

def twototen(arr):
    number = 0
    for j in range(1, len(arr) + 1):
        number += (arr[-j] * (2 ** (j - 1)))
    return number


data = list(map(int, input()))
# print(data)

result = []
for i in range(len(data) // 7):
    arr = data[(7 * i) : (7 * (i + 1))]
    # print(arr)
    result.append(twototen(arr))

print(result)


