# 괄호가 정상적이면 True, 아니면 False
# target은 괄호 검사 대상 문자열
def check_bracket(target):
    # 여는 괄호가 나오면, stack에 push
    # 닫는 괄호가 나오면 stack에서 pop
    # 문장이 끝났을 때, stack이 비어있으면 정상적인 괄호
    # 아니라면 비정상 괄호
    # abcde(def(ef)eadfadsf)asdfadsf
    stack = list()
    for i in range(len(target)):
        # 문자가 여는 괄호라면 push
        # 닫는 괄호면 pop, pop할게 없으면(비어있으면) False
        if target[i] == "[" or target[i] == "{" or target[i] == "(":
            stack.append(target[i])
        elif target[i] == "]" or target[i] == "}" or target[i] == ")":
            if len(stack) == 0: # 비어 있음
                return False
            else:
                tmp = stack.pop() # 비어있지 않으면 pop하고, 짝이 맞는지 검사 해야한다.
                if target[i] == "]" and tmp == "[":
                    continue
                elif target[i] == "}" and tmp == "{":
                    continue
                elif target[i] == ")" and tmp == "(":
                    continue
                ### 여기까지 진입하면 무슨 의미?? ###
                # 스택은 비어있지 않은데, 짝이 맞지 않음.
                return False

    # 반복문이 끝났을 때 stack이 비어있으면 True
    # 아니면 False
    if len(stack) != 0:
        return False
    else:
        return True

str = "({])"
result = check_bracket(str)
print(result)

