def selection(a, k):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

    # k번째로 작은 것
    # return a[k-1]
    # k번째로 큰것
    # return a[k]
    # 중앙값
    return a[len(a)//2]




arr = [64, 25, 10, 22, 11]
print(selection(arr, 2))
print(selection(arr, -2))

