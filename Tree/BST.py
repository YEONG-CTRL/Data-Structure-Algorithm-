class Node():
    def __init__(self, data):
        self.left  = None
        self.right = None
        self.data  = data

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return 
        else:
            current_node = self.root
            while True: 
                # Just keep lopping everytime
                # to avoid infinite loop, return으로  exit  
                if value < current_node.data: # 왼쪽으로
                    if current_node.left == None: 
                        current_node.left = new_node
                        return # None point 하면 exit
                    else:
                        current_node = current_node.left # 차있으면 현재노드 변경
                
                elif value > current_node.data: # 오른쪽으로
                    if current_node.right == None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
                

    def lookup(self,value): # 모든 node를 iterate하지 않음, O(1og N)
        if self.root == None: #lookup 불가
            return None    
        else: 
            current_node = self.root # A
            while current_node: #1. current_node가 None 될대때까지 돌거나.
                if value < current_node.data:
                    current_node = current_node.left
                elif value > current_node.data:
                    current_node = current_node.right
                elif current_node.data == value: #2. current_node값이 value와 같아질때까지 돌거나
                    return current_node



            # while True: # B
            #     if value > current_node.data:
            #         current_node = current_node.right
            #         if current_node.right == None:
            #             return None  # 52~53 / 56~57 라인은 while current_node: 로 대체 가능
            #     elif value < current_node.data:
            #         current_node = current_node.left
            #         if current_node.left == None:
            #             return None 
            #     elif value == current_node.data:
            #             return current_node
        

bst = BinarySearchTree()
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
x = bst.lookup(6)
print(x)


