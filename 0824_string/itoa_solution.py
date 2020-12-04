def itoa(num):
    x = num # 몫
    y = 0  # 나머지
    arr = []
    while x:
        y = x % 10
        x = x // 10 # x //= 10
        arr.append(chr(y + ord("0")))
        arr.append(y) # 숫자를 받아 리스트로 변환

    arr.reverse()

    str1 = "".join(map(str, arr))
    return str1
    # return arr

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))