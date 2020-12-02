

class node():
    def __init__(self, num):
        self.num = num
        self.right = None
        self.left = None
    
    def inorder_trav(self, _node, ht):
        if _node == None:
            return
        if not _node.left == None:
            self.inorder_trav(_node.left, ht+1)
        inorder.append((_node.num, ht))
        if not _node.right == None:
            self.inorder_trav(_node.right, ht+1)
        


root = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node6 = node(6)
node7 = node(7)

root.left = node2; root.right = node3
node2.left = node4; node2.right = node5
node3.left = node6; node3.right = node7

inorder = []
root.inorder_trav(root,0)

print(inorder)
a = 4; b = 7

min_ht = float('inf')
min_ind = -1
found_first = False
found_sec = False

for i in range(len(inorder)):
    if inorder[i][0] == a:
        found_first = True
    if inorder[i][0] == b:
        found_sec = True
    if found_first and not found_sec:
        if min_ht> inorder[i][1]:
            min_ht = inorder[i][1]
            min_ind = i
    
print(inorder[min_ind][0])