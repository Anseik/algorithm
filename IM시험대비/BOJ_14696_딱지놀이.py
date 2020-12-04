import sys
sys.stdin = open('BOJ_14696_딱지놀이.txt')

T = 2
for tc in range(1, T + 1):
    N = int(input())
    for round in range(N):
        a_info = list(map(int, input().split()))
        b_info = list(map(int, input().split()))

        a_dict = {4:0, 3:0, 2:0, 1:0}
        b_dict = {4:0, 3:0, 2:0, 1:0}
        for i in range(1, len(a_info)):
            a_dict[a_info[i]] += 1

        for i in range(1, len(b_info)):
            b_dict[b_info[i]] += 1

        # print(a_dict)
        # print(b_dict)


        for key in range(4, 0, -1):
            if a_dict[key] > b_dict[key]:
                print("A")
                break
            elif a_dict[key] < b_dict[key]:
                print("B")
                break
        else:
            print("D")