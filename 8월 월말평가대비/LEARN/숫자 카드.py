import sys
sys.stdin = open("숫자 카드.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input()
    # print(N)
    # print(cards)

    count = [0] * 10
    for i in range(N):
        count[int(cards[i])] += 1

    # print(count)
    max_count = 0
    max_card = 0
    for j in range(len(count)):
        if count[j] >= max_count:
            max_count = count[j]
            max_card = j

    print("#{} {} {}".format(tc, max_card, max_count))