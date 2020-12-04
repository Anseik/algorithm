import sys
sys.stdin = open('GNS.txt')

num_sys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for _ in range(T):
    tc, N = input().split()
    N = int(N)
    # print(tc, N)
    num_list = input().split()

    trans_num_list = []
    for i in range(N):
        trans_num_list.append(num_sys.index(num_list[i]))

    trans_num_list.sort()

    print(tc)
    for j in range(N):
        print(num_sys[trans_num_list[j]], end=" ")
    print()