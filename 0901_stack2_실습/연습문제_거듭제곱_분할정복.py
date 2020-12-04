# 거듭제곱 : 밑수와 거듭제곱 수를 입력받아서 결과를 반환하는 함수작성
# 재귀 --> 기저부 / 실행부
def power(base, exponent):
    if exponent == 0 or base == 0:
        return 1

    # exponent 제곱수가 짝수
    if exponent % 2 == 0:
        new_base = power(base, exponent // 2)
        return new_base * new_base
    # exponent 제곱수가 홀수
    else:
        new_base = power(base, (exponent - 1) // 2)
        return new_base * new_base * base



result = power(0, 8)
print(result)