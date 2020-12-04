def bubble(arr):
    for i in range(len(arr)-1, 0, -1): # 4, 3, 2, 1
        for j in range(i): # 0, 1, 2, 3
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [10, 44, 3, 23, 1, 5, 21]
result = bubble(arr)
print(result)