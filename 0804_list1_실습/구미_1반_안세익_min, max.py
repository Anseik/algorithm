# import sys
# sys.stdin = open()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 초기값은 항상 이유가 있어야 한다.
    min = numbers[0]
    max = numbers[0]
    result = 0
    for i in numbers:
        if i < min:
            min = i

    for j in numbers:
        if j > max:
            max = j

    result = max - min

    print('#%d' % tc, result)