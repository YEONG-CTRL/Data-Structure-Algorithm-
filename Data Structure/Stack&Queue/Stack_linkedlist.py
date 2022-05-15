class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top    = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        if not self.top:
            return None
        return self.top.data
    
    def push(self,data):
        newtop = Node(data)
        if self.length == 0:
            self.top = newtop
            self.bottom = self.top
            self.length = 1
        else:
            prev = self.top
            self.top = newtop
            self.top.next = prev
            self.length += 1
    
    def pop(self):
        if not self.top:
            return None 
        if self.length == 1:
            self.top = None
            return self.top
        prev = self.top
        newtop = self.top.next
        newsec = self.top.next.next
        self.top = newtop
        self.top.next = newsec
        self.length -= 1
        return prev
    
    def printall(self):
        node = self.top
        arr = []
        while node:
            print(node.data, end = " ->")
            node = node.next
        print()

stck = Stack()
stck.push(3)
stck.push(5)
stck.push(7)
stck.push(8)
stck.push(9)
stck.pop()


stck.pop()

print(stck.peek())
stck.printall()
