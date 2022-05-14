class Node():
    def __init__(self,data):
        self.data    = data
        self.pointer = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length  = 0

    def append(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = self.head
            self.length += 1
        else:
            self.tail.pointer = newnode # 이전 tail이 newnode를 가리키고
            self.tail         = newnode # tail을 바꿈
            self.length       += 1

    def prepend(self,data):
        newnode = Node(data)
        newnode.pointer = self.head
        self.head = newnode

        self.length += 1      
    
    def insert(self,index,data):
        newnode = Node(data)
        i = 0
        temp = self.head
        if index >= self.length:
            self.append(newnode)
            return 
        
        if index == 0:
            self.prepend(data)
            return
        
        while i < self.length:
            if i == index-1:
                temp.pointer, newnode.pointer = newnode, temp.pointer
                self.length += 1
                break
            temp = temp.pointer
            i += 1
            

    def delete(self,index):
        temp = self.head
        i = 0 

        if index >= self.length:
            print("wrong index")
        
        if index == 0:
            self.head = self.head.pointer
            self.length -= 1
            return 

        while i < self.length:
            if i == index-1:
                temp.pointer = temp.pointer.pointer
                self.length -= 1
                break
            i += 1
            temp = temp.pointer

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.pointer
        


ll = LinkedList()

ll.append(3)
ll.append(5)
ll.append(6)
ll.append(7)
ll.prepend(8)
ll.insert(2,100)
ll.insert(5, 80)
ll.delete(3)
ll.print()