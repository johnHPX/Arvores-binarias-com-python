class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class AVLNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.height = 0
