# 정렬이 안된 경우
def seq_search(a, n, k):
    i = 0
    while i < n and a[i] != k:
        i += 1
    if i < n: return i
    else : return False

arr = [4, 9, 11, 23, 2, 7]
key = 23
print(seq_search(arr, len(arr), key))

# 정렬이 된 경우
# def seq_search(a, n, k):
#     i = 0
#     while i < n and a[i] < k:
#         i += 1
#     if a[i] == k: return i
#     else: return False
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# key = 10
# print(seq_search(arr, len(arr), key))