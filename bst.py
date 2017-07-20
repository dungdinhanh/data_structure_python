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


#
# def fucntion(a, b):
#     return a-b
#
# new_bst = BST(8)
# new_bst.insert_node(5)
# new_bst.insert_node(6)
# new_bst.insert_node(6)
# new_bst.insert_node(8)
# new_bst.insert_node(9)
# new_bst.insert_node(10)
# new_bst.insert_node(11)
#
# new_bst.in_order_traversal()
# print("\n")
# newNode = new_bst.search_node(5)
# print(newNode.data)
# newNode = new_bst.search_node(8)
# print(newNode.data)
# print("\n")
# new_bst.delete_node(5)
# #print(data.data)
# new_bst.in_order_traversal()
# print("\n")
# new_bst.delete_node(8)
# new_bst.in_order_traversal()
# print("\n")
# new_bst.delete_node(6)
# new_bst.in_order_traversal()
# print("pre order")
# new_bst.pre_order_traversal()
# print(" post order")
# new_bst.post_order_traversal()