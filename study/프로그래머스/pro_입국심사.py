def solution(n, times):
    s, e = 1, (max(times) * n) # 이론상 최선, 최악의 심사시간
    answer = 0
    while s <= e:
        m = (s + e) // 2 # 이진탐색, 중간값
        judge = 0 # 심사한 사람 수
        for time in times: # 심사대마다 m분 동안 몇 사람을 심사할 수 있는지 계산하여 judge에 합한다.
            judge += (m // time)
            if judge >= n:
                answer = m
                e = m -1 # 최소 시간이 m보다 짧으므로 e를 m - 1로 바꿔 while문을 계속 돈다.
                break
        else:
            s = m + 1 # 최소 시간이 m보다 길기때문에 s를 m + 1로 바꿔 while문을 계속 돈다.

    return answer


def solution2(n, times):
    s, e = 0, (max(times) * n) # 이론상 최선, 최악의 심사시간
    answer = 0
    while s <= e:
        m = (s + e) // 2 # 이진탐색, 중간값
        judge = 0 # 심사한 사람 수
        for time in times:
            judge += (m // time) # 심사대마다 m분 동안 몇 사람을 심사할 수 있는지 계산하여 judge에 합한다.
            if judge >= n:
                answer = m
                e = m - 1
                break

        if judge < n:
            s = m + 1

    return answer

n = 6
times = [7, 10]

result = solution2(n, times)
print(result)