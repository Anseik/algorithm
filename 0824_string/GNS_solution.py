def gns_sort(numbers):
    # global numbers
    numbers_dic = {
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

    for i in range(1, len(numbers)): # 첫번째 패스부터 N-1번째 패스
        for j in range(len(numbers)-i): # 각 패스당 정렬할 횟수
            if numbers_dic[numbers[j]] > numbers_dic[numbers[j+1]]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

import sys
sys.std = open("GNS.txt")

T = int(input())
for t in range(T):
    tc, N = input().split()
    N = int(N)
    # 정렬을 하기 위해서는 대소 비교를 해야하는데
    # 글자를 그냥 그대로 가지고는 대소비교가 안됨
    # 대소비교를 위해서 dictionary를 사용
    # {"ZRO": 0, "ONE": 1 ...}
    numbers = input().split()
    gns_sort(numbers)
    print(tc)
    print(tc, *numbers)

