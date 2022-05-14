class hash_table():
    def __init__(self,size):
        self.size = size
        self.data = [None] * self.size
    
    def __str__(self):
        return str(self.__dict__)
    
    def _hash(self,key): # custom hash function
        return len(key) % self.size
    
    def put(self,key,value): # insert a new key,value pair
        has = self._hash(key)
        if not self.data[has]:
            self.data[has] = [[key,value]]
        else:
            self.data[has].append([key,value])

    def get(self,key): # return the value of the key 
        has = self._hash(key)
        if self.data[has]: # collision
            for i in range(len(self.data[has])):
                if self.data[has][i][0] == key:
                    return self.data[has][i][1]
        return None

    def keys(self): # return all keys
        keys_array = []
        for i in range(self.size):
            if self.data[i]: # self.data의 요소들 중 비어있지 않다면
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array

    def remove(self,key):
        has = self._hash(key)
        for i in range(len(self.data[has])):
            if self.data[has][i][0] == key:
                a = self.data[has].pop(i)
                return a
        return None

h = hash_table(10)
h.put('grapes',1000)
h.put('apples',10)
h.put('ora',300)
h.put('banan',200)
print(h)
print(h.get('ora'))
print(h.keys())
h.remove('ora')
print(h)
print(h.keys())
