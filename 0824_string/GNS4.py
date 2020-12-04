import sys
sys.stdin = open('GNS.txt')

num_sys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for _ in range(T):
    tc, N = input().split()
    N = int(N)
    num_str = input()

    print(tc)
    for num in num_sys:
        print((num + ' ') * num_str.count(num), end='')
    print()