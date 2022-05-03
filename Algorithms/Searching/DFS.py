class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self,val):
    new_node = Node(val)
    if self.root == None:
      self.root = new_node
      return 
    temp = self.root
    while True:
      if new_node.val < temp.val:
        if temp.left == None:
          temp.left = new_node
          break
        else:
          temp = temp.left
      elif new_node.val > temp.val:
        if temp.right == None:
          temp.right = new_node
          break
        else:
          temp = temp.right

  def lookup(self,val):
    temp = self.root
    while True:
      if temp.val == val:
        return True
      elif temp == None:
        return False
      elif val < temp.val:
        temp = temp.left
      elif val > temp.val:
        temp = temp.right

  def dfsinorder(self,currnode,mylist):
    if currnode != None:
      self.dfsinorder(currnode.left,mylist) #child가 있으면 traverse all the way down
      mylist.append(currnode.val)
      self.dfsinorder(currnode.right,mylist)
    return mylist #list of nodes(sorted)

  def dfspreorder(self,currnode,mylist):
    if currnode!=None:
      mylist.append(currnode.val) 
      self.dfspreorder(currnode.left,mylist) #stack으로 함수를 쌓음
      self.dfspreorder(currnode.right,mylist)
    return mylist

  def dfspostorder(self,currnode,mylist):
    if currnode.left:
      self.dfspostorder(currnode.left,mylist)
    if currnode.right:
      self.dfspostorder(currnode.right,mylist)
    mylist.append(currnode.val)
    return mylist
    
      
    

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# print(tree.dfsinorder(tree.root,[]))
# print(tree.dfspreorder(tree.root,[]))
print(tree.dfspostorder(tree.root,[]))

#     9 
#  4     20
#1  6  15  170


#inorder: 1 4 6 9 15 20 170
#preorder: 9 4 1 6 20 15 170
#postorder: 1 6 4 15 170 20 9