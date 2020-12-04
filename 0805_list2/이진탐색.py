def bin_search(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start + end) // 2
        # 키값과 미들이 같은 경우
        if a[middle] == key:
            return True, middle
        # 키값이 미들보다 작은경우
        elif a[middle] > key:
            end = middle -1
        # 키값이 미들보다 큰경우
        else:
            start = middle + 1

    return False, -1

arr = [2, 4, 7, 9, 11, 19, 23]
key = 7
print(bin_search(arr, key))