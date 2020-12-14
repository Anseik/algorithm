import sys
from string import ascii_lowercase
S = sys.stdin.readline().strip()

def make_suffixnum_list(text):
    # 접미사 리스트 생성
    suffix_li = []
    for i in range(len(text)):
        suffix_li.append((text[i:].strip(), i))
    suffix_li.sort()
    # print(suffix_li)

    # 접미사 번호 리스트 생성
    num_li = []
    for j in range(len(suffix_li)):
        num_li.append(suffix_li[j][1])
    # print(num_li)

    return num_li


def make_arr(idx):
    global result
    # 같은 접미사 배열을 만드는 문자열 T가 이미 존재하면 리턴
    if result == 1:
        return

    if idx == len(S):
        text = ''.join(text_li)
        # text는 S와는 다르고 같은 접미사 배열을 만들어야 한다.
        if text != S and S_li == make_suffixnum_list(text):
            result = 1
        return

    for i in range(len(alpha)):
        # 사전순으로 같거나 앞설때만 재귀호출
        if alpha[i] <= S[idx]:
            text_li[idx] = alpha[i]
            make_arr(idx + 1)
            text_li[idx] = ''


alpha = list(ascii_lowercase)
# print(alpha)

S_li = make_suffixnum_list(S)
# print(S_li)


text_li = [''] * len(S)
# print(text_li)

result = 0
make_arr(0)

print(result)



