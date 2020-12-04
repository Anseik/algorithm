# 숫자 123을 문자 123으로 변환 단, str() 미사용

# 숫자를 하나씩 분리해 문자로 만들기

# >>1, 2, 3(어려움)
# >>3, 2, 1(쉬움)

# 숫자를 하나씩 분리할 때는 %(modular)연산을 사용

# 뒤에서부터 분리하는 법
# 123 // 10 = 12, 123 % 10 = 3
# 12 // 10 = 1, 12 % 10 = 2
# 1 // 10 = 0, 1 % 10 = 1

# 앞에서부터 분리하는 법
# 123 % 100 = 23
# 123 // 100 = 1(1분리)
# 23 % 10 = 3
# 23 // 10 = 2(2분리)
# 3 % 1 = 0
# 3 // 1 = 3(3분리)

################################################
def itoa(number):
    # 해야할 일 : 숫자를 한자리씩 잘라서 문자열로 만들기
    # 123 >> 123//100, 23//10, 3//1
    # 자리수를 알아야 한다.
    # 1. 대상 숫자의 자리수에 따라 divider(ex. 1, 10, 100)를 구한다.
    # 2. 대상 숫자를 divider로 나누어 몫을 취해 문자열에 추가하고 나머지를 다음 대상 숫자로 한다.
    # 3. 대상 숫자가 0이 되면 종료한다.

    # 1. divider 구하기
    divider = 1
    while True:
        tmp = divider * 10
        if tmp > number:
            break
        divider = tmp

    # 2. 대상 숫자를 divider로 나누어 몫을 취해 문자열에 추가하고 나머지를 다음 대상 숫자로 한다.
    result=""
    while number > 0:
        quotient = number // divider
        remain = number % divider
        divider = divider // 10
        # 몫을 문자열로 만들어서 더해주기
        result += chr(quotient+48)
        number = remain

    return result

a = 12345
b = itoa(a)
print(type(b))
print(b)

