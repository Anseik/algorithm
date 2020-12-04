import sys
sys.stdin = open('Flatten.txt')

T = 10
for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # print(dump)
    # print(boxes)
    while dump > 0:
        max_box = boxes[0]
        max_index = 0
        min_box = boxes[0]
        min_index = 0
        for i in range(len(boxes)):
            if boxes[i] > max_box:
                max_box = boxes[i]
                max_index = i

        for j in range(len(boxes)):
            if boxes[j] < min_box:
                min_box = boxes[j]
                min_index = j

        boxes[max_index] -= 1
        boxes[min_index] += 1
        dump -= 1

    final_max_box = boxes[0]
    final_min_box = boxes[0]
    for box in boxes:
        if box > final_max_box:
            final_max_box = box

    for box in boxes:
        if box < final_min_box:
            final_min_box = box

    result = final_max_box - final_min_box

    print('#%d' %tc, result)



