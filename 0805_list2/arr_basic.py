# 2차원배열 반복문으로 접근하기
# 2차원 배열 : 배열의 원소가 배열인 형태
# [[], [], [], []]

arr = [[1, 2, 3], [4, 5, 6, 7], [8, 9], [10]]
# 길이가 4인 2차원 배열
# arr의 길이 : 4
# 순회하면서 arr의 모든 원소의 합구하기

sum_v = 0
for i in range(len(arr)):
    # print(arr[i])
    for j in range(len(arr[i])):
        sum_v += arr[i][j]
print(sum_v)


