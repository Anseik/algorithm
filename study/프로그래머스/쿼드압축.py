def solution(arr):
    answer = [0, 0]
    size = len(arr[0])
    for r in range(size):
        for c in range(size):
            if arr[r][c] == 0:
                answer[0] += 1
            else:
                answer[1] += 1

    # 쿼드 압축 실행
    def press(size, r, c):
        num = arr[r][c]
        can = True
        for i in range(r, r + size):
            for j in range(c, c + size):
                if arr[i][j] != num:
                    can = False
                    break
            if not can:
                break

        if can:
            answer[num] -= (size ** 2 - 1)
        else:
            if size >= 4:
                ns = size // 2
                for d in range(4):
                    if d == 0:
                        press(ns, r, c)
                    elif d == 1:
                        press(ns, r, c + ns)
                    elif d == 2:
                        press(ns, r + ns, c)
                    elif d == 3:
                        press(ns, r + ns, c + ns)

    press(size, 0, 0)

    return answer