# 최대 크기가 정해져 있는 queue
class Queue:
    # 데이터를 뺄때는, front에서 빼고 데이터를 추가할때는 rear에 추가
    def __init__(self, n):
        self.q = [0] * n
        self.front = -1
        self.rear = -1

    def enQueue(self, d):
        self.rear += 1
        self.q[self.rear] = d

    def deQueue(self):
        self.front += 1
        return self.q[self.front]


my_queue = Queue(10)
my_queue.enQueue(5)
my_queue.enQueue(4)
my_queue.enQueue(3)
my_queue.enQueue(2)
my_queue.enQueue(1)
print(my_queue.deQueue())
print(my_queue.deQueue())
print(my_queue.deQueue())
print(my_queue.deQueue())
print(my_queue.deQueue())
