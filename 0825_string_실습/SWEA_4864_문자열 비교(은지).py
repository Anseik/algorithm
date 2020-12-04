T = int(input())
for tc in range(1, T+1):
    A = input()
    B = input()

    def brute(p, t):
        i, j = 0, 0
        while j < len(p) and i < len(t):
            if t[i] != p[j]:
                i = i - j
                j = -1
            i += 1
            j += 1
        if j == len(p):
            return 1
        else:
            return 0


    print("#{} {}".format(tc, brute(A, B)))
