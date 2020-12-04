
def check_babyjin(num):
    c = [0] * 10
    for i in range(6):
        c[num % 10] += 1
        num //= 10

    # print(c)
    i = 0
    tri = run = 0
    while i < 10:
        # triplet 검사
        if c[i] >= 3:
            tri += 1
            c[i] -= 3
            continue

        # run 검사
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            run += 1
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            continue

        # babyjin 검사
        if tri + run == 2:
            return True

        # 아직 babyjin이 아니면 i를 증가시키며 계속 탐색
        i += 1

    # while문이 끝났는데 babyjin이 아니면 False를 반환
    return False

num = 456456
if check_babyjin(num): print('BabyJIn입니다.')
else: print('BabyJin이 아닙니다.')