# 재귀를 이용한 이진탐색
# def bin_search(a, s, e, k):
#     if s > e: return False
#     else:
#         m = (s + e) // 2
#         if k == a[m]:
#             return True, m
#         # k가 a[m]보다 작을때
#         elif k < a[m]:
#             e = m - 1
#             return bin_search(a, s, e, k)
#         # k가 a[m]보다 클 때
#         else:
#             s = m + 1
#             return bin_search(a, s, e, k)
#
#
# arr = [2, 4, 7, 9, 11, 19, 23]
# key = 7
# print(bin_search(arr, 0, len(arr)-1, key))


def bin_search(a, k):
    s = 0
    e = len(a) - 1
    while s <= e:
        m = (s + e) // 2
        if k == a[m]:
            return True, m
        elif k < a[m]:
            e = m - 1
        else:
            s = m + 1

    return False

arr = [2, 4, 7, 9, 11, 19, 23]
key = 8
print(bin_search(arr, key))