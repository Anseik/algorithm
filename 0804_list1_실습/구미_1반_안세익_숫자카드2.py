import sys
sys.stdin = open('card.txt')

T = int(input())
for tc in range(1, T+1):
    card = int(input())
    numbers = input()
    counts = [0] * 10

    for number in numbers:
        # print(number)
        counts[int(number)] += 1

    max_card = 0
    max_count = 0
    for i in range(len(counts)):
        if counts[i] >= max_count:
            max_count = counts[i]
            max_card = i

    print('#%d' %tc, max_card, max_count)

