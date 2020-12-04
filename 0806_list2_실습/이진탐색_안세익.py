import sys
sys.stdin = open('이진탐색.txt')

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # print(P, Pa, Pb)
    start = 1
    end = P

    cnt_A = 0
    while start <= end:
        # 찾는 값이 middle과 같은 경우
        cnt_A += 1
        middle = (start + end) // 2
        if Pa == middle:
            # print(cnt_A)
            break
        # 찾는 페이지가 middle보다 큰 경우
        elif Pa > middle:
            start = middle
        # 찾는 페이자가 middle보다 작은 경우
        else:
            end = middle

    start = 1
    end = P
    cnt_B = 0
    while start <= end:
        # 찾는 값이 middle과 같은 경우
        cnt_B += 1
        middle = (start + end) // 2
        if Pb == middle:
            # print(cnt_B)
            break
        # 찾는 페이지가 middle보다 큰 경우
        elif Pb > middle:
            start = middle
        # 찾는 페이자가 middle보다 작은 경우
        else:
            end = middle

    if cnt_A < cnt_B:
        result = 'A'
    elif cnt_B < cnt_A:
        result = 'B'
    else:
        result = 0

    print('#%d' %tc, result)

    # 함수로 만들어서 사용해보자
    def binarySearch(s, e, key):
        l, r = s, e
        cnt = 0
        while l <= r:
            mid int((l+r) / 2)
            cnt += 1
            if key == mid:
                break
            elif key < mid:
                r = mid
            else:
                l = mid

        print(cnt)


