'''
3 3
1 2 3
4 5 6
7 8 9
'''

# 1
# N, M = map(int, input().split())
# mylist = [0 for _ in range(N)]
# # mylist = [0] * N
#
# for i in range(N):
#     mylist[i] = list(map(int, input().split()))
# print(mylist)

# 2
# N, M = map(int, input().split())
# mylist = []
# for i in range(N):
#     mylist.append(list(map(int, input().split())))
# print(mylist)

# 3
# N, M = map(int, input().split())
# print(N)
# print(M)
# mylist = [list(map(int, input().split())) for _ in range(N)]
# print(mylist)

# 0으로 초기화
# N = 3 # 행
# M = 4 # 열
# 열을 먼저 만든다.
# v = [[0 for _ in range(M)] for _ in range(N)]
# v = [[0] * M for _ in range(N)]
# print(v)

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(i+1, M):
#         # if i < j:
#         arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
# print(arr)

# 1, 2, 3, 4(조합으로 만들기)
arr = [1, 2, 3, 4]
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        # if i < j:
        # arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        print(arr[i], arr[j], end=" ")

