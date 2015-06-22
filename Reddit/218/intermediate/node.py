class Node:

    def __init__(self):
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

    

    def __str__(self):
        string = "["

        if (self.left is not None):
            string += "Node"
        string += ", "

        if (self.right is not None):
            string += "Node"
        string += ", "

        if (self.top is not None):
            string += "Node"
        string += ", "

        if (self.bottom is not None):
            string += "Node"
        string += "]"
        return string;

    def addLeft(self, node):
        self.left = node
        node.right = self

    def addRight(self, node):
        self.right = node
        node.left = self

    def addTop(self, node):
        self.top = node
        node.bottom = self

    def addBottom(self, node):
        self.bottom = node
        node.bottom = self
