class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def insert_node(self, data):
        if self.data:
            if self.data < data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert_node(data)
            elif self.data > data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert_node(data)
            else:
                self.data = data
        else:
            self.data = data

    def search_node(self, data):
        if self.data:
            if self.data < data and self.right is not None:
                node = self.right.search_node(data)
            elif self.data > data and self.left is not None:
                node = self.left.search_node(data)
            elif self.data == data:
                node = self
            else:
                node = None
            return node
        else:
            return None

    def find_min(self, node):
        if node is None:
            return
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp

    def delete_node(self, data):
        if self.data is None:
            return None
        if data < self.data and self.left is not None:
            self.left = self.left.delete_node(data)
        elif data > self.data and self.right is not None:
            self.right = self.right.delete_node(data)
        elif data == self.data == 0:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            node = self.find_min(self.right)
            self.data = node.data
            self.right = self.right.delete_node(node.data)
            return self
        return self

    def pre_order_traversal(self):
        if self.data is None:
            return
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        if self.data is None:
            return
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        if self.data is None:
            return
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data)


