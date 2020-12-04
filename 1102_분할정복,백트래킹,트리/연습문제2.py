
def powerset(idx, cursum):
    if idx == N:
        if cursum == 10:
            result = []
            for i in range(N):
                if select[i]:
                    result.append(arr[i])
            print(result)
        return

    select[idx] = 1
    powerset(idx + 1, cursum + arr[idx])
    select[idx] = 0
    powerset(idx + 1, cursum)


arr = [1,2,3,4,5,6,7,8,9,10]
N = len(arr)
select = [0] * N
powerset(0, 0)

