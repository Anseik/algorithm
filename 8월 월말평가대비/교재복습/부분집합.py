arr = [1, 2, 3]

n = len(arr)

power_set = []
for i in range(1<<n): # 부분집합의 개수, 비트정보
    sub_set = []
    for j in range(n): # 비트검사
        if i & (1<<j): # i의 j번째 비트가 1인지 확인
            sub_set.append(arr[j])
    power_set.append(sub_set)

print(power_set)