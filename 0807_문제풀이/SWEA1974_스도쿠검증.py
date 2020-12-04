T = int(input())
n = 9
for tc in range(1, T+1):
    mylist = [list(map(int, input().split())) for _ in range(n)]
    #print(mylist)
    h_cnt = [0] * (n+1)  #9칸만들면 인덱스가 0~8 이니까 그냥 10칸 만들어서 0인덱스를 버리고 1~9를 쓰자.
    v_cnt = [0] * (n+1)
    s_cnt = [0] * (n+1)

    result = 1

    for i in range(n):
        h_cnt = [0] * (n + 1)
        v_cnt = [0] * (n + 1)
        for j in range(n):
            h_cnt[mylist[i][j]] += 1
            v_cnt[mylist[j][i]] += 1
        for k in range(1, n+1):
            if h_cnt[k] != 1 or v_cnt[k] != 1:
                result = 0

    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            Size = 3
            s_cnt = [0] * (n + 1)
            for a in range(i, i+Size):
                for b in range(j, j+Size):
                    s_cnt[mylist[a][b]] += 1
            for k in range(1, n):
                if s_cnt[k] != 1:
                    result = 0

    print('#{} {}'.format(tc, result))