from nodes import AVLNode
from binaryTree import BinaryTree

class AVLTree(BinaryTree):
    def __max(self, a, b):
        if a > b:
            return a
        else:
            return b

    def __node_height(self, node:AVLNode):
        if node is None:
            return -1
        else:
            return node.height

    def __balancing_factor(self, node:AVLNode):
        if node:
            return (self.__node_height(node.left)) - (self.__node_height(node.right))
        else:
            return 0

    def __update_height(self, node: AVLNode):
        node.height = self.__max(self.__node_height(node.left), self.__node_height(node.right)) + 1

    def __left_rotation(self, node:AVLNode):
        y = node.right
        f = y.left

        y.left = node
        node.right = f

        self.__update_height(node)
        self.__update_height(y)

        return y

    def __right_rotation(self, node: AVLNode):
        y = node.left
        f = y.right

        y.right = node
        node.left = f

        self.__update_height(node)
        self.__update_height(y)

        return y

    def __right_left_rotation(self, node:AVLNode):
        node.right = self.__right_rotation(node.right)
        return self.__left_rotation(node)

    def __left_right_rotation(self, node:AVLNode):
        node.left = self.__left_rotation(node.left)
        return self.__right_rotation(node)

    def __balance(self, node:AVLNode):
        fb = self.__balancing_factor(node)

        if fb < -1 and self.__balancing_factor(node.right) <= 0:
            node = self.__left_rotation(node)

        elif fb > 1 and self.__balancing_factor(node.left) >= 0:
            node = self.__right_rotation(node)

        elif fb > 1 and self.__balancing_factor(node.left) < 0:
            node = self.__left_right_rotation(node)

        elif fb < -1 and self.__balancing_factor(node.right) > 0:
            node = self.__right_left_rotation(node)

        return node

    def __insert_node(self, node:AVLNode, value):
        if not node:
            return AVLNode(value)
        elif value < node.data:
            node.left = self.__insert_node(node.left, value)
        else:
            node.right = self.__insert_node(node.right, value)

        self.__update_height(node)
        node = self.__balance(node)
        return node

    def insert(self, value):
        if not self.root:
            self.root = AVLNode(value)
        else:
            self.root = self.__insert_node(self.root, value)


    def __remove_node(self, node:AVLNode, value):
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

        self.__update_height(node)
        node = self.__balance(node)
        return node

    def remove(self, value):
        if self.root is None:
            return None
        else:
            self.root = self.__remove_node(self.root, value)
