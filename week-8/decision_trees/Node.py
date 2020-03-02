#Trevor O'Hearn 2/28/20
#Basic Node class for Trees
#has two pointers to left and right nodes
class Node():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
    def __init__(self, x, left=None, right=None):
        self.data = x
        self.left = left
        self.right = right
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

    def setValue(self, x):

    # def setLeft(self, node):
    #     if (isInstance(node, Node)):
    #         self.left = node
    #     else:
    #         raise Exception('Not a Node', 'illegal')
    # def setRight(self, node):
    #     if (isInstance(node, Node)):
    #         self.right = node
    #     else:
    #         raise Exception('Not a Node', 'illegal')
    def getData(self):
        return self.data
    # def setData(self, x):
    #     self.data = x
    def isLeaf(self):
        return (self.left == None and self.right == None)
    def print(self):
        print(self.data)
