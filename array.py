class Myarray:
    def __init__(self):
        self.length = 0
        self.data   = {}

    def get(self,index):
        return self.data[index]

    def push(self, value):
        self.data[self.length] = value
        self.length            += 1
        return self.length
        
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item
    
    def shift_items(self,index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1

    def delete(self,index):
        delete_item = self.data[index]
        self.shift_items(index)

        
newarray = Myarray()
newarray.push("first")
newarray.push("second")
newarray.push("third")
newarray.push("four")
newarray.delete(1)
print(newarray)