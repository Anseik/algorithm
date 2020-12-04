import sys
sys.stdin = open('최고의 쌍.txt')

def comb(idx, cnt, multiply):
    global result
    if cnt == 2:
        # 모듈러 연산으로 뒤에서부터 숫자를 가져와 1씩 감소하는지 확인한다.
        quo, com = divmod(multiply, 10)
        while quo >= 10: # 한자리 숫자일때는 확인할 필요없다.
            quo, rem = divmod(quo, 10)
            if com - 1 != rem:
                return
            com = rem

        # while문에서 return 되지 않으면 연속으로 증가한다는 조건을 만족
        # 가장 큰 multiply를 result에 저장한다.
        if multiply > result:
            result = multiply

        return

    if idx == N:
        return

    comb(idx + 1, cnt + 1, multiply * numbers[idx])
    comb(idx + 1, cnt, multiply)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = -1
    comb(0, 0, 1)

    print("#{} {}".format(tc, result))