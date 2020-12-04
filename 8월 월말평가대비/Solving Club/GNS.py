import sys
sys.stdin = open('GNS.txt')

num_sys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for _ in range(T):
    tc, N = input().split()
    int(N)
    num_list = input().split()
    # print(num_list)
    trans = []
    for num in num_list:
        trans.append(num_sys.index(num))
    # print(trans)

    trans.sort()
    print(tc)
    for t in trans:
        print(num_sys[t], end=" ")
    print()
