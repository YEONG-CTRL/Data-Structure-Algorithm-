from collections import deque


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first  = None
        self.last   = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            return None
        return self.first.data

    def enqueue(self,value):
        newnode = Node(value)
        if self.last == None: # empty queue
            self.last = newnode
            self.first  = self.last
            self.length += 1
        else:
            self.last.next = newnode # 1->2->3 에서 기존 self.last는 3, 이때 4를 추가한다고 가정하면, 3의 next로 4를 지정 
            self.last = newnode     # 원래 3이던 self.last를 4로 변경
            self.length += 1
        
    def dequeue(self):
        if self.last == None: # 큐가 비었는지 확인
            return None
        if self.last == self.first: # 큐에 원소 하나
            self.last = None

        self.first = self.first.next # 1->2->3에서, 맨 앞의 1을 2로 바꿈
        self.length -= 1

    def printall(self):
        node = self.first
        while node:
            print(node.data, end=' -> ')
            node = node.next
        print()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.printall()
q.dequeue()
q.printall()
print(q.peek())
