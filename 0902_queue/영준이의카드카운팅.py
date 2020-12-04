import sys
sys.stdin = open('영준이의카드카운팅.txt')


def empty_card(string, cards):
    global error

    # 행 순회를 하며 있는 카드의 위치에 1을 저장한다. 중복하여 카드가 있으면 error를 True로 하고 반복문을 종료
    for i in range(cards):
        r = pattern[string[3*i]]
        tmp = ""
        tmp = tmp + string[3*i+1] + string[3*i+2]
        num = int(tmp)
        if check[r][num] == 0:
            check[r][num] = 1
        else:
            error = True
            break

T = int(input())
for tc in range(1, T+1):
    string = input()
    # print(string)
    cards = len(string) // 3 # 입력받은 문자열에서 카드의 개수, 문자3개가 하나의 카드를 나타낸다.

    # 에러여부 확인
    error = False

    # 체크 배열을 만들어 놓고 S, D, H, C순으로 각 행마다 해당 카드가 있는지 저장한다.
    check = [[0] * 14 for _ in range(4)] # 0번 인덱스는 사용하지 않는다.
    # 0번 행 : S, 1번행 : D, 2번행 : H, 3번행 : C
    pattern = {"S": 0, "D": 1, "H": 2, "C": 3} # 무늬에 따라 몇번째 행인지 확인하기 위한 딕셔너리

    # 함수실행
    empty_card(string, cards)

    # 오류시 출력
    if error == True:
        print("#{} {}".format(tc, 'ERROR'))

    # 정상인 경우 출력
    else:
        print("#{}".format(tc), end=" ")
        for y in range(4):
            cnt = 0
            for x in range(1, 14):
                if check[y][x] == 0:
                    cnt += 1
            print(cnt, end=" ")
        print()