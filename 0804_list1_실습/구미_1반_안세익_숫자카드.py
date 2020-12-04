# import sys
# sys.stdin = open()

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers_str = input()
    numbers = []
    for number in numbers_str:
        numbers.append(number)

    # print(numbers)

    card_dict = {}
    for i in numbers:
        if i not in card_dict.keys():
            card_dict[i] = 1

        else:
            card_dict[i] += 1

    # print(card_dict)

    max_key = 0
    max_val = 0
    for key, val in card_dict.items():
        if val > max_val:
            max_val = val
            max_key = int(key)
        elif val == max_val:
            if int(key) > max_key:
                max_key = int(key)

    print('#%d' %tc, max_key, max_val)


        # print(type(int(key)))
        # print(type(val))
