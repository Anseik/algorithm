# 숫자 형태의 문자열을 받아 숫자로 변환
def atoi(str):
    value = 0
    for i in range(len(str)):
        c = str[i]
        # 0 ~ 9
        # if c >= "0" and c <= "9":
        if "0" <= c <= "9": # 파이썬은 가능
            digit = ord(c) - ord("0")
        else:
            break
        value = value * 10 + digit
        # value = value * 10 + ord(c) - ord("0")
        # 숫자형태의 문자열인 경우 바로 위와 같이 사용 가능
    return value

a = "123"
print(a, type(a))

b = atoi(a)
print(b, type(b))


# 요소가 숫자인 리스트를 입력받아 하나의 숫자로 변환
def atoi_arr(str):
    value = 0
    for i in range(len(str)):
        c = str[i]
        value = value * 10 + c
    return value

arr1 = [1, 2, 3]
int1 = atoi_arr(arr1)
print(int1, type(int1))
