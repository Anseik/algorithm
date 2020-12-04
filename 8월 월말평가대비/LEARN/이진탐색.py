import sys
sys.stdin = open('이진탐색.txt')

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # print(P, Pa, Pb)

    # A의 경우
    s, e, k = 1, P, Pa
    cnt_a = 0
    while s <= e:
        cnt_a += 1
        m = (s + e) // 2
        if k == m:
            break
        elif k < m:
            e = m
        else:
            s = m

    # B의 경우
    s, e, k = 1, P, Pb
    cnt_b = 0
    while s <= e:
        cnt_b += 1
        m = (s + e) // 2
        if k == m:
            break
        elif k < m:
            e = m
        else:
            s = m

    result = ""
    if cnt_a < cnt_b:
        result += "A"
    elif cnt_b < cnt_a:
        result += "B"
    else:
        result += "0"

    print("#{} {}".format(tc, result))