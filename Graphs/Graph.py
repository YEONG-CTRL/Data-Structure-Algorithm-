# Graph 표현하는 방법들 

# 1. Edge List
graph1 = [[0,2],[2,3],[2,1],[1,3]]
# Simply Shows the connection

# 2.Adjacent List
graph2 = [[2], [2,3], [0,1,3], [1,2]]
# 0번인덱스(0번 노드)는 2번 노드와 연결, 1번인덱스는 2,3번 노드와연결....

# 3. Adjacent Matrix
graph3 = [
    [0,0,1,0],
    [0,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]
# nodex가 node y 에 연결돼 있는지 나타내는 0과 1만 있음

class Graph(): #Undirected, Unweighted Graph / Adjacenct List로 만듬(hash table사요)    
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list  = {}
    
    def insert_node(self,node):
        if node not in self.adjacent_list:
            self.adjacent_list[node] = []
            self.number_of_nodes     += 1
        

    def insert_edge(self,node1,node2):
        if node2 not in self.adjacent_list[node1]: #한쪽에 없으면 반대편에도 없음
            self.adjacent_list[node1].append(node2)
            self.adjacent_list[node2].append(node1)
        else:
            return "node already exists"

    def show_connections(self):
        for node, neighbors in self.adjacent_list.items():#unpack위해 .items()사용
            print(node, end="-->")
            print(' '.join(str(neighbors)))


my_graph = Graph()
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_node(4)

my_graph.insert_edge(1,2)
my_graph.insert_edge(1,3)
my_graph.insert_edge(2,3)
my_graph.insert_edge(4,1)

my_graph.show_connections()