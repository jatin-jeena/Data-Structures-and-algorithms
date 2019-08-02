class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None
    def addData(self,data):
        self.data = data
    def addLeftChild(self,leftchild):
        self.leftChild = leftchild
    def addRightChild(self,rightchild):
        self.rightChild = rightchild
    def inorderTraversal(self):
        if self.leftChild != None:
            self.leftChild.inorderTraversal()
        print(self.data)
        if self.rightChild != None:
            self.rightChild.inorderTraversal()
    def postOrderTraversal(self):
        if self.leftChild != None:
            self.leftChild.postOrderTraversal()

        if self.rightChild != None:
            self.rightChild.postOrderTraversal()
        print(self.data)
    def preOrderTraversal(self):
        print(self.data)
        if self.leftChild != None:
            self.leftChild.preOrderTraversal()

        if self.rightChild != None:
            self.rightChild.preOrderTraversal()

root = Node()
root.addData(49)
left = Node()
left.addData(78)
right = Node()
right.addData(90)
root.addLeftChild(left)
root.addRightChild(right)


#inorder traversal
root.inorderTraversal()

#Preorder traversal
root.preOrderTraversal()

#postorder traversal
root.postOrderTraversal()