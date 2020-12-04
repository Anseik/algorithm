arr = [1, 2, 3]

N = len(arr)

for i in range(1<<N): # 부분집합의 개수
    for j in range(N): # 원소의 수만큼 비트를 비교함
        if i & (1 << j): # i
            print(arr[j], end=",")
    print()
print()