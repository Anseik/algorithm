import sys
sys.stdin = open('영준이의카드카운팅.txt')

T = int(input())
for tc in range(1, T+1):
    cards = input()
    # 카드 무늬별로 카드를 세기 위한 배열생성
    # 무늬 S, D, H, C
    s_arr = [0] * 14
    d_arr = [0] * 14
    h_arr = [0] * 14
    c_arr = [0] * 14

    result = False # 카운팅이 정상종료 되었는지 표시
    for i in range(0, len(cards), 3):
        shape = cards[i]
        number = int(cards[i+1:i+3])
        if shape == 'S':
            if s_arr[number] == 1:
                break
            s_arr[number] = 1
            s_arr[0] += 1
        elif shape == 'D':
            if d_arr[number] == 1:
                break
            d_arr[number] = 1
            d_arr[0] += 1
        elif shape == 'H':
            if h_arr[number] == 1:
                break
            h_arr[number] = 1
            h_arr[0] += 1
        elif shape == 'C':
            if c_arr[number] == 1:
                break
            c_arr[number] = 1
            c_arr[0] += 1
    else:
        # 겹치는 카드 없이 정상종료
        result = True

    if result: # 정상종료, 카운팅이 잘 끝난경우
        print("#{} {} {} {} {}".format(tc, 13-s_arr[0], 13-d_arr[0], 13-h_arr[0], 13-c_arr[0]))

    else:
        print("#{} ERROR".format(tc))