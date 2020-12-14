import sys
for line in sys.stdin:
    s, e = map(int, line.rstrip().split())

    if not (2 <= s <= 9 and 2 <= e <= 9):
        print('INPUT ERROR!')

    else:

        for i in range(1, 10):
            # print(i)
            if s < e:
                for j in range(s, e + 1):
                    r = j * i
                    if 0 < r < 10:
                        r = ' ' + str(r)
                    print("{} * {} = {}".format(j, i, r), end="   ")


            else:
                for j in range(s, e - 1, -1):
                    r = j * i
                    if 0 < r < 10:
                        r = ' ' + str(r)
                    print("{} * {} = {}".format(j, i, r), end="   ")

            print()


