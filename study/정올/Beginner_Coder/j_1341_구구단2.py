import sys
for line in sys.stdin:
    s, e = map(int, line.strip().split())

    if s < e:
        for i in range(s, e + 1):
            for j in range(1, 10):
                r = i * j
                if 0 < r < 10:
                    r = ' ' + str(r)
                if j % 3:
                    print("{} * {} = {}".format(i, j ,r), end="   ")
                else:
                    print("{} * {} = {}".format(i, j, r))
            print()

    else:
        for i in range(s, e - 1, -1):
            for j in range(1, 10):
                r = i * j
                if 0 < r < 10:
                    r = ' ' + str(r)
                if j % 3:
                    print("{} * {} = {}".format(i, j ,r), end="   ")
                else:
                    print("{} * {} = {}".format(i, j, r))
            print()
