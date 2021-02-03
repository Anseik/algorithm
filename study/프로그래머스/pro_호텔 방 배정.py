import sys
sys.setrecursionlimit(10 ** 6)

room_dict = dict()

def find_empty(wish):
    # 내가 원하는 방이 아직 배정되지 않았으면 바로 그 방을 배정
    if wish not in room_dict:
        room_dict[wish] = wish + 1
        return wish

    # 내가 원하는 방이 이미 배정되었으면 조건에 맞는 빈 방을 찾는다.
    else:
        # 빈방을 찾을때까지 재귀 호출
        empty = find_empty(room_dict[wish])
        # 빈방을 찾고나면 value값(어떤 방이 이미 배정되어 있을때 다음으로 비어있는지 확인해야하는 방 번호)을 갱신한다.
        room_dict[wish] = empty + 1
        return empty


def solution(k, room_number):
    answer = []
    for wish in room_number:
        result = find_empty(wish)
        answer.append(result)

    return answer

k = 10
room_number = [1,3,4,1,3,1]

print(solution(k, room_number))