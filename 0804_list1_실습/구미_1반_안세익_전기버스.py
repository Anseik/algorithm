import sys
sys.stdin = open('전기버스.txt')

T = int(input())
for tc in range(1, T + 1):
    main_info = list(map(int, input().split()))  # [3, 10, 5]
    stop_info = list(map(int, input().split()))  # [1, 3, 5, 7, 9]
    road = list(range(0, main_info[1]+1))

    cnt = 0
    position = 0

    while position < main_info[1] - main_info[0]:
        for j in range(main_info[0], 0, -1):
            if (position+j) in stop_info:
                cnt += 1
                position += j
                break
        else:
            cnt = 0
            break

    print('#%d' %tc, cnt)

