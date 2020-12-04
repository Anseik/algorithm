import sys
sys.stdin = open('글자수.txt')

T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()
    m = len(p)
    n = len(t)
    # print(p, t, m, n)

    str_dict = {}
    for i in range(n):
            str_dict[t[i]] = 1
        if t[i] not in str_dict:
        else:
            str_dict[t[i]] += 1
    # print(str_dict)

    max = 0
    for j in range(m):
        if str_dict[p[j]] > max:
            max = str_dict[p[j]]

    print("#{} {}".format(tc, max))
