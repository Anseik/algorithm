T = int(input())

code = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}

for test_case in range(1, T+1):
    tc, cnt = input().split()
    cnt = int(cnt)
    num = list(input().split())
    # print(tc, cnt)
    for i in range(cnt-1):
        index = i
        for j in range(i+1, cnt):
            if code[num[index]] > code[num[j]]:
                index = j
        num[i], num[index] = num[index], num[i]
    print(tc)
    for i in num:
        print(i,end=' ')
    print()