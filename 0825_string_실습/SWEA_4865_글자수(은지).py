T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    max = 0
    for str in str1:
        if str2.count(str) > max:
            max = str2.count(str)

    print("#{} {}".format(tc, max))