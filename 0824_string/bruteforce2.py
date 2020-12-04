str = "Hello world! Nice to meet you"
pattern = "llo"

# target 안에서 pattern을 찾으면 True, 아니면 False 반환
# [][][][][][] : 6
#       [][][] : 3
# len(target) - len(pattern) + 1
def search(target, pattern):
    for i in range(len(target) - len(pattern) + 1):
        for j in range(len(pattern)):
            # 똑같으면 다음거 비교 진행
            # 다르면 다음 i 반복문으로 넘어간다.
            if pattern[j] != target[i+j]:
                break
        else: # j 반복문에서 break가 안 걸리면, 패턴을 찾은 것
            return True, i

    return False

result = search(str, pattern)
print(result)



