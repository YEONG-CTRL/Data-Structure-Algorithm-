class stack:
    def __init__(self):
        self.array = []
        self.length = 0

    def __str__(self):
        return str(self.__dict__)
    
    def peek(self):
        if self.length == 0:
            return None
        return self.array[len(self.array)-1]
        
    def push(self,data):
        self.array.append(data)
        self.length += 1

    def pop(self):
        a = self.array[self.length-1]
        del self.array[self.length-1]
        self.length -= 1
        return a

    def printall(self):
        for i in self.array:
            print(i, end='-->')

stck = stack()
stck.push(1)
stck.push(2)
stck.push(3)
stck.push(4)
stck.pop()
stck.pop()
stck.pop()

print(stck.peek())
stck.printall()