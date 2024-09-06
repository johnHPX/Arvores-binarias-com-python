from nodes import Node

class BinaryTree:
    def __init__(self):
        self.root = None

    def __print_node_pre_order(self, node:Node):
        if node:
            print(node.data,end=" ")
            self.__print_node_pre_order(node.left)
            self.__print_node_pre_order(node.right)

    def print_pre_order(self):
        if self.root:
            self.__print_node_pre_order(self.root)
            print()
        else:
            return None

    def __print_node_in_order(self, node:Node):
        if node:
            self.__print_node_in_order(node.left)
            print(node.data,end=" ")
            self.__print_node_in_order(node.right)

    def print_in_order(self):
        if self.root:
            self.__print_node_in_order(self.root)
            print()
        else:
            return None

    def __print_node_pos_order(self, node:Node):
        if node:
            self.__print_node_pos_order(node.left)
            self.__print_node_pos_order(node.right)
            print(node.data,end=" ")

    def print_pos_order(self):
        if self.root:
            self.__print_node_pos_order(self.root)
            print()
        else:
            return None

    def __print_tree(self, node, space = 0):
        count = 5
        if node is None:
            return

        space += count
        self.__print_tree(node.right, space)

        print()
        for i in range(count, space):
            print(end=" ")
        print(f"{node.data}\n")

        self.__print_tree(node.left, space)

    def print_tree(self, space = 0):
        if self.root:
            self.__print_tree(self.root, space)
        else:
            return None

    def _search_min_node(self, node:Node):
        while node.left:
            node = node.left
        return node

    def search_minimum(self):
        if self.root:
            return self._search_min_node(self.root)
        else:
            return None

    def __search_max_node(self, node:Node):
        while node.right:
            node = node.right
        return node

    def search_maximum(self):
        if self.root:
            return self.__search_max_node(self.root)
        else:
            return None

    def __search_node(self, node:Node, value):
        if not node:
            return None
        elif value < node.data:
            return self.__search_node(node.left, value)
        elif value > node.data:
            return self.__search_node(node.right, value)
        else:
            return node

    def search(self, value):
        if self.root is None:
            return None
        else:
            return self.__search_node(self.root, value)
