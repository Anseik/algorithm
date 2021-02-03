def solution(new_id):
    answer = ''
    new_id_li = list(new_id)

    # 1단계(대문자 -> 소문자)
    new_id_li = [i.lower() for i in new_id_li]

    # 2단계(알파벳 소문자, 숫자, 뺴기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    new_id_li = [i for i in new_id_li if i not in s_li]

    # 3단계(new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    before = ''
    i = 0
    while i < len(new_id_li):
        if before == '.' and new_id_li[i] == '.':
            new_id_li.pop(i)
        else:
            before = new_id_li[i]
            i += 1

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(new_id_li) >= 1 and new_id_li[0] == '.':
        new_id_li.pop(0)
    if len(new_id_li) >= 1 and new_id_li[-1] == '.':
        new_id_li.pop(-1)

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not new_id_li:
        new_id_li.append('a')

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new_id_li) >= 16:
        new_id_li = new_id_li[0:15]
    if new_id_li[-1] == '.':
        new_id_li.pop(-1)

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id_li) < 3:
        new_id_li.append(new_id_li[-1])

    # 결과
    answer = "".join(new_id_li)
    return answer

new_id = 'abcdefghijklmn.p'
s = '~!@#$%^&*()=+[{]}:?,<>/'
s_li = [i for i in s]
print(solution(new_id))