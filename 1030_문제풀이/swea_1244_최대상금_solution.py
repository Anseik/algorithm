import sys
sys.stdin = open('swea_1244_최대상금_solution.txt')


T = int(input())
for tc in range(1, T + 1):
    arr, cnt = input().split()
    cnt = int(cnt)
    arr = list(map(str, arr))

    N = len(arr)
    ans = 0
    visit = [set() for _ in range(11)]
    # 탐색의 깊이(visit의 인덱스)마다 만들어진 num을 저장한다.
    # num이 이미 생성되어 있으면 탐색을 중단한다(백트래킹)
    # num 아래로 만들어지는 숫자들 역시 이미 탐색되어 있는 숫자이기때문이다.
    def backtrack(k): # 현재 교환 횟수
        global ans

        num = int(''.join(arr))
        if num in visit[k]:
            return
        else:
            visit[k].add(num)

        if k == cnt:
            if ans < num:
                ans = num

        else: # 조합을 for문 중첩으로 생성
            for i in range(N - 1): # 2개를 선택해야 하므로 최소 1개는 남겨놓는다.
                for j in range(i + 1, N): # 위에서 선택한것 다음부터 선택가능
                    arr[i], arr[j] = arr[j], arr[i]
                    backtrack(k + 1)
                    arr[i], arr[j] = arr[j], arr[i]

    backtrack(0)
    print('#{} {}'.format(tc, ans))



# 5C3
# arr = ['A', 'B', 'C', 'D', 'F']
# N = len(arr)
# for i in range(N - 2): # 뒤에 최소 2개를 남겨놓는다.
#     for j in range(i + 1, N - 1): # 뒤에 최소 1개를 남겨놓는다.
#         for k in range(j + 1, N):
#             print(arr[i], arr[j], arr[k])