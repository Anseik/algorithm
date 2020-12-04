# atoi('1234') -> 1234

def atoi(str):
    result = 0
    is_negative = False

    for i in range(len(str)):
        if i == 0 and str[i] == "-":
            is_negative = True
            continue
        tmp = ord(str[i]) - ord("0")
        # 숫자 형태의 문자를 숫자로 변환하기 위해서 ord("1") - ord("0") = 1 형태로 작성
        # ord("1")은 49이고 ord("0")은 48이므로 빼면 숫자 1이 나온다.
        result = (result * 10) + tmp
    if is_negative:
        result = -result

    return result

str1 = "-1234"
int1 = atoi(str1)
print(int1, type(int1))