import sys
sys.stdin = open('Flatten.txt')

T = 10
for tc in range(1, T+1):
    D = int(input())
    boxes = list(map(int, input().split()))
    # print(D)
    # print(boxes)


    while D:
        max = boxes[0]
        min = boxes[0]
        max_idx = 0
        min_idx = 0
        for i in range(len(boxes)):
            #가장 큰것과 가장 작은 것을 찾아 가장 큰것에서 -1 가장 작은것에서 +1한다.
            if boxes[i] > max:
                max = boxes[i]
                max_idx = i
            if boxes[i] < min:
                min = boxes[i]
                min_idx = i

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        D -= 1

    max_result = boxes[0]
    min_result = boxes[0]
    for j in range(len(boxes)):
        if boxes[j] > max_result:
            max_result = boxes[j]
        if boxes[j] < min_result:
            min_result = boxes[j]

    result = max_result - min_result


    print("#{} {}".format(tc, result))