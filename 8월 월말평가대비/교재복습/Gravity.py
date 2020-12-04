boxes = [7, 4, 2, 0, 0, 6, 0, 7, 0]

max_cnt = 0
for i in range(0, len(boxes)-1): # 대상
    target = boxes[i]
    cnt = 0
    for j in range(i+1, len(boxes)): # 비교
        if target > boxes[j]:
            cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)