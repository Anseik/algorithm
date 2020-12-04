boxes = [7, 4, 2, 0, 0, 6, 0, 7, 0]

# 상자로 채워진 방이있다.
# 방을 오른쪽으로 90도 회전 시켰을 때,
# 낙차가 가장 큰 상자의 낙차를 구하여라

# 각 줄의 가장높이 있는 상자의 낙차가 각줄에서 가장 크다.
# 상자의 낙차는 어떻게 구할 것인가?
# 낙차를 구하는 방법 : 현재 오른쪽이 비어있거나 높이가 자신보다 작은상자이면,
# 원래 모양에서 오른쪽에 있는 상자의 높이가 현재대상보다 작거나 상자가 쌓여있지 않으면 낙차를 증가

# 모든 열의 낙차를 구하고, 그 중에서 가장 큰 값을 반환(출력)한다.
# max나 min값을 저장하는 변수를 선언 할때는 분명한 이유가 있어야 한다.

max_cnt = 0
for i in range(0, len(boxes)-1):
    target = boxes[i]
    cnt = 0
    for j in range(i+1, len(boxes)): # 1번열부터 끝까지 순회
        if target > boxes[j]:
            cnt += 1
    print(cnt)

    # print(cnt)
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)