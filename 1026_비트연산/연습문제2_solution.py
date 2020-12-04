# 48 ~ 57 >>> 숫자 : 변환없이 그냥 반환
# 65 ~ 70 >>> 10이상, 아스키 코드 이용해서 변환 후 반환
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

str = '328D1AF6E4C9BB'

result = list()
for i in range(len(str)):
    number = hex_to_decimal(str[i])
    result += decimal_to_binary(number)
# print(len(result))
print(result)

for i in range(0, len(result), 7):
    tmp = result[i : i + 7]
    ind = 0
    num = 0
    for i in range(len(tmp) - 1, -1, -1):
        if tmp[i] == 1:
            num += (2 ** ind)
        ind += 1
    print(num, end=" ")