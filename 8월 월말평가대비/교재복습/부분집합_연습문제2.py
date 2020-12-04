def check_sub_set(arr):
    n = len(arr)
    power_set = []
    for i in range(1 << n):
        sub_set = []
        for j in range(n):
            if i & (1 << j):
                sub_set.append(arr[j])
        power_set.append(sub_set)

    for i in range(len(power_set)):
        if sum(power_set[i]) == 0 and power_set[i]:
            print(power_set[i])
            return True
    return False

arr = [-7, -3, 5, 8]
result = check_sub_set(arr)
print(result)