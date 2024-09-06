from nodes import Node
from binaryTree import BinaryTree

class BinarySearchTree(BinaryTree):
    def __insert_node(self, node:Node, value):
        if not node:
            return Node(value)
        elif value < node.data:
            node.left = self.__insert_node(node.left, value)
        else:
            node.right = self.__insert_node(node.right, value)

        return node

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root = self.__insert_node(self.root, value)


    def __remove_node(self, node:Node, value):
        if node is None:
            return None

        if value < node.data:
            node.left = self.__remove_node(node.left, value)
        elif value > node.data:
            node.right = self.__remove_node(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = super()._search_min_node(node.right)
                node.data = temp.data
                node.right = self.__remove_node(node.right, temp.data)

        return node

    def remove(self, value):
        if self.root is None:
            return None
        else:
            self.root = self.__remove_node(self.root, value)
