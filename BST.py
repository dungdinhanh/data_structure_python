import tree_node


class BST:
    def __init__(self, data=None):
        self.root = tree_node.TreeNode(data)

    def insert_node(self, data):
        self.root.insert_node(data)

    def delete_node(self, data):
        if self.root is None:
            return
        self.root = self.root.delete_node(data)

    def search_node(self, data):
        temp = self.root.search_node(data)
        return temp

    def in_order_traversal(self):
        if self.root is None:
            return
        self.root.in_order_traversal()

    def pre_order_traversal(self):
        if self.root is None:
            return
        self.root.pre_order_traversal()

    def post_order_traversal(self):
        if self.root is None:
            return None
        self.root.post_order_traversal()



# def fucntion(a, b):
#     return a-b
#
# bst = BST(8)
# bst.insert_node(5, fucntion)
# bst.insert_node(6, func_cmp=fucntion)
# bst.insert_node(6, fucntion)
# bst.insert_node(8, fucntion)
# bst.insert_node(9, fucntion)
# bst.insert_node(10, fucntion)
# bst.insert_node(11, fucntion)
#
# bst.in_order_traversal()
# print("\n")
# newNode = bst.search_node(5,func_cmp=fucntion)
# print(newNode.data)
# newNode = bst.search_node(8, func_cmp=fucntion)
# print(newNode.data)
# print("\n")
# bst.delete_node(5, func_cmp=fucntion)
# #print(data.data)
# bst.in_order_traversal()
# print("\n")
# bst.delete_node(8, func_cmp=fucntion)
# bst.in_order_traversal()
# print("\n")
# bst.delete_node(6, func_cmp=fucntion)
# bst.in_order_traversal()