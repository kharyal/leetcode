class node():
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None
    
    def dfs(self, _node, target_node):
        if _node == None:
            return False
        
        if _node.num == target_node:
            return True
        r1 = False; r2 = False

        if not _node.left == None:
            r1 = self.dfs(_node.left, target_node)
        
        if not _node.right == None:
            r2 = self.dfs(_node.right, target_node)
        
        if r1 or r2:
            print(_node.num)

        return r1 or r2
    
    def non_recursive_dfs(self, target_num):
        
        call_arr = [-1]*10

        while len(stack)>0:
            nd = stack.pop()
            if nd.num == target_num:
                break

            if not nd.right == None:
                stack.append(nd.right)
                call_arr[nd.right.num] = nd.num 
            if not nd.left == None:
                stack.append(nd.left)
                call_arr[nd.left.num] = nd.num

        parent = call_arr[target_num]
        
        while parent>-1:
            print(parent)
            parent = call_arr[parent]


root = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node6 = node(6)
node7 = node(7)

root.left = node2

stack = [root]