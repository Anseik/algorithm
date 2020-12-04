class Node(): # 연결리스트에서 하나의 요소를 저장할 객체를 만드는 클래스
    # 데이터 하나를 저장할 공간(변수)
    # 다음 노드의 주소를 저장할 변수

    def __init__(self, d):
        self.d = d
        self.next = None # 다음 노드를 가리키는 변수, 다음 노드는 아직 모르니 일단 변수만 생성

    def set_next(self, next):
        self.next = next

class LinkedList():
    # 노드들이 연결되어 있는 리스트
    # 가장 앞쪽에 있는 노드(head)에 대한 정보만을 가지고 있다.
    # size
    def __init__(self):
        # variable annotation
        self.head: Node # head라는 변수의 타입을 미리 지정
        self.head = None
        self.size = 0

    # 삽입, 삭제, 조회, pop
    def append(self, data): # 마지막에 노드 추가
        # 마지막 노도에 새로운 노드를 만들어서 연결
        new_node = Node(data)
        current = self.head # 가지고 있는게 head밖에 없다.
        if current == None: # 데이터가 없음
            self.head = new_node
        else:
            # 아니면 마지막 노드를 찾아서 마지막 노드의 next에
            # 새로운 노드를 연결해주면 된다.
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def delete(self, idx): # 해당 인덱스 데이터 삭제
        current = self.head

        # 지우려는 node가 head일 경우는?
        if idx == 0: # head를 지우려고 한다.
            self.head = current.next

        # 이전 노드의 next를 지우려는 노드의 next로 변경해주면 된다.
        for i in range(idx - 1):
            current = current.next

        current.next = current.next.next
        self.size -= 1

    def get(self, idx): # 해당 인덱스 데이터 조회
        current = self.head
        for i in range(idx):
            current = current.next
        return current.d

    def pop(self): # 마지막 노드 삭제 / 반환
        prev = self.head

        for i in range(self.size - 2):
            prev = prev.next

        last = prev.next
        prev.next = None
        self.size -= 1
        return last.d


my_list = LinkedList()
my_list.append('a')
my_list.append('b')
my_list.append('c')
my_list.append('d')
my_list.append('e')
my_list.append('f')


for i in range(my_list.get_size()):
    print(my_list.get(i), end = " ")
print()
print(my_list.get_size())
my_list.pop()
my_list.pop()
for i in range(my_list.get_size()):
    print(my_list.get(i), end = " ")