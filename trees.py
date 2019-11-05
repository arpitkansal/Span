class Node:
    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None

    def insert(self, x):
            if x > self.data:
                if self.right is None:
                    self.right = Node(x)
                else:
                    self.right.insert(x)
            elif x < self.data:
                if self.left is None:
                    self.left = Node(x)
                else:
                    self.left.insert(x)
    def printInorder(self):
        if self.left:
            self.left.printInorder()
        print(self.data)
        if self.right:
            self.right.printInorder()
    lDepth = -1
    rDepth = -1
def height(node):
        if(node is None):
            return -1
        else:
            lDepth = height(node.left)
            rDepth = height(node.right)

            if (lDepth > rDepth):
                return (lDepth + 1)
            else:
                return (rDepth + 1)

class Tree:

    def __init__(self):
        self.root = None

    def insertdata(self,x):
        self.root.insert(x)

    def printTree(self):
        self.root.printInorder()

    def findHeight(self):
        return self.root.height()



rt = Node(15)
t = Tree()
t.root = rt
t.insertdata(10)
t.insertdata(20)
t.insertdata(25)
#t.insertdata(16)
h= height(rt)

print(h)


