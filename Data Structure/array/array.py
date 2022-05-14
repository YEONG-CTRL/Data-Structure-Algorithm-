class Myarray:
    def __init__(self):
        self.length = 0
        self.data   = {}

    def __str__(self):
        return str(self.__dict__)

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
newarray.push("five")

print(newarray)


def reverse(array):
    leng = array.length
    point = leng // 2

    if array.length % 2 == 0:
        for i in range(point):
            array.data[i], array.data[leng-1-i] = array.data[leng-1-i],array.data[i]
        return array
    
    else:
        for i in range(point+1):
            array.data[i], array.data[leng-1-i] = array.data[leng-1-i],array.data[i]
        return array


reverse = reverse(newarray)
print(reverse)