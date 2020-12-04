# idx : 인덱스
# used : 이미 순열을 만드는데 사용되었는지 체크하는 배열
# perm_arr : 순열을 저장할 배열
def perm(used, perm_arr, idx):
    #순서를 만들어야할 요소의 개수
    if idx >= N:
        print(perm_arr)
        return

    #반복문 돌면서, 이전에 사용하지 않은 요소들을 이용해서 순열 만들기
    for i in range(N):
        if used[i] == 0:    #사용되지 않은 요소라면,
            perm_arr[idx] = arr[i]      # 순열에 포함시키기
            used[i] = 1 # 해당 요소를 사용했음을 표시
            perm(used, perm_arr, idx+1)
            used[i] = 0 # 원래대로 되돌려 주기

arr = [1,2,3,4,5]
N = len(arr)
used = [0] * N
perm_arr = [0] * N
perm(used, perm_arr, 0)
