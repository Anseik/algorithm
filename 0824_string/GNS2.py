import sys
sys.stdin = open('GNS.txt')

trans = [('ZRO', 0), ('ONE', 1), ('TWO', 2), ('THR', 3), ('FOR', 4), ('FIV', 5), ('SIX', 6), ('SVN', 7), ('EGT', 8), ('NIN', 9)]
# print(trans[1][0])

T = int(input())
for tc in range(1,T+1):
    info = input()
    n = int(info[3:])
    # print(n, type(n))
    numbers = input()
    numbers = numbers.replace('ZRO', '0')
    numbers = numbers.replace('ONE', '1')
    numbers = numbers.replace('TWO', '2')
    numbers = numbers.replace('THR', '3')
    numbers = numbers.replace('FOR', '4')
    numbers = numbers.replace('FIV', '5')
    numbers = numbers.replace('SIX', '6')
    numbers = numbers.replace('SVN', '7')
    numbers = numbers.replace('EGT', '8')
    numbers = numbers.replace('NIN', '9')
    # print(numbers, type(numbers))
    numbers_list = numbers.split(" ")
    # print(numbers_list)

    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if numbers_list[j] < numbers_list[min]:
                min = j
        numbers_list[i], numbers_list[min] = numbers_list[min], numbers_list[i]
    # print(numbers_list, type(numbers_list))

    new_numbers = " ".join(numbers_list)
    # print(new_numbers)
    new_numbers = new_numbers.replace('0', 'ZRO')
    new_numbers = new_numbers.replace('1', 'ONE')
    new_numbers = new_numbers.replace('2', 'TWO')
    new_numbers = new_numbers.replace('3', 'THR')
    new_numbers = new_numbers.replace('4', 'FOR')
    new_numbers = new_numbers.replace('5', 'FIV')
    new_numbers = new_numbers.replace('6', 'SIX')
    new_numbers = new_numbers.replace('7', 'SVN')
    new_numbers = new_numbers.replace('8', 'EGT')
    new_numbers = new_numbers.replace('9', 'NIN')

    print('#%d' %tc)
    print(new_numbers)





