
class node():
    def __init__(self, num):
        self.num = num
        self.parent = None

node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node6 = node(6)

def union(n1, n2):
    if n1.parent ==None and n2.parent == None:
        par_node = node(n1.num)
        n1.parent = par_node
        n2.parent = par_node
    
    elif n1.parent == None:
        n1.parent = n2.parent
        
    elif n2.parent == None:
        n2.parent = n1.parent

union(node2, node3)
union(node1, node2)
union(node5, node6)

for nodes in [node1, node2, node3, node4, node5, node6]:
    if not nodes.parent == None:
        print(nodes.parent.num)
    else:
        print(-1)