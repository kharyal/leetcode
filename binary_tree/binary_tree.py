class node():
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None
    
    def dfs(self, _node):
        if _node == None:
            return
        print(_node.num)
        if not _node.left == None:
            self.dfs(_node.left)
        if not _node.right == None:
            self.dfs(_node.right)

    def dfs_loop(self, _node):

        stack = []
        stack.append(_node)

        while stack:
            nd = stack.pop()
            print(nd.num)
            if not nd.right == None:
                stack.append(nd.right)
            if not nd.left == None:
                stack.append(nd.left)

    def inorder_trav(self, _node):
        if _node == None:
            return
        if not _node.left == None:
            self.inorder_trav(_node.left)
        print(_node.num)
        if not _node.right == None:
            self.inorder_trav(_node.right)

    def bfs(self, _node):

        q = []
        q.append(_node)

        while q:
            nd = q.pop(0)
            print(nd.num)
            if not nd.left == None:
                q.append(nd.left)
            if not nd.right == None:
                q.append(nd.right)

    def dfs_print_path(self, _node, target_num):
        if _node == None:
            return False
        if _node.num == target_num:
            print(_node.num)
            return True
        # print(_node.num)
        r1 = False
        r2 = False
        if not _node.left == None:
            r1 = self.dfs_print_path(_node.left, target_num)
        if not _node.right == None:
            r2 = self.dfs_print_path(_node.right, target_num)
        
        if r1 or r2:
            print(_node.num)
        
        return r1 or r2 
            
            
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

root.dfs_print_path(root, 4)