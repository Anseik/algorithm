import sys
sys.stdin = open('GNS.txt')

trans = [('ZRO', 0), ('ONE', 1), ('TWO', 2), ('THR', 3), ('FOR', 4), ('FIV', 5), ('SIX', 6), ('SVN', 7), ('EGT', 8), ('NIN', 9)]
# print(trans[1][0])

T = int(input())
for tc in range(1,T+1):
    info = input()
    n = int(info[3:])
    # print(n, type(n))
    numbers = input()
    # print(numbers, type(numbers))
    numbers_list = numbers.split(" ")
    # print(numbers_list)

    for i in range(n):
        for j in range(len(trans)):
            if numbers_list[i] == trans[j][0]:
                numbers_list[i] = trans[j][1]

    for k in range(0, n-1):
        # 최소값 찾기
        min = k
        for l in range(k+1, n):
            if numbers_list[l] < numbers_list[min]:
                min = l
        numbers_list[k], numbers_list[min] = numbers_list[min], numbers_list[k]

    for m in range(n):
        for n in range(len(trans)):
            if numbers_list[m] == trans[n][1]:
                numbers_list[m] = trans[n][0]

    result = " ".join(numbers_list)

    print('#%d' %tc)
    print(result)




