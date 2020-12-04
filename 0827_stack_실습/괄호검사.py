import sys
sys.stdin = open('괄호검사.txt')

# tip : 딕셔너리로 짝을 미리 맞춰놓는다.

def bracket(target):
    stack = list()
    for i in range(len(target)):
        if target[i] == "(" or target[i] == "{": # 여는 괄호이면 스택에 추가
            stack.append(target[i])

        # 닫는 괄호이면 스택에서 top을 pop해서 닫는 괄호와 짝이 맞는지 비교
        elif target[i] == ")" or target[i] == "}":
            if len(stack) == 0: # 스택이 비어있으면
                return 0 # 괄호의 짝이 맞지 않으므로 0을 반환
            else:
                temp = stack.pop()
                if temp == "(" and target[i] == ")":
                    continue
                elif temp == "{" and target[i] == "}":
                    continue
                else:
                    return 0

    if len(stack) != 0:
        return 0
    return 1



T = int(input())
for tc in range(1, T+1):
    target = input()
    # print(target)
    result = bracket(target)




    print("#{} {}".format(tc, result))