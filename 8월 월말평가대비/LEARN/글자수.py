import sys
sys.stdin = open('글자수.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    # print(str1)
    # print(str2)

    check = {}
    for i in range(len(str1)):
        if str1[i] not in check:
            check[str1[i]] = 0

    # print(check)

    for j in range(len(str2)):
        if str2[j] in check:
            check[str2[j]] += 1

    max_cnt = 0
    for val in check.values():
        if val > max_cnt:
            max_cnt = val

    print("#{} {}".format(tc, max_cnt))