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

def height(node):
        if (node is None):
            return 0
        else:
            lDepth = height(node.left)
            rDepth = height(node.right)

            if (lDepth > rDepth):
                return (lDepth + 1)
            else:
                return (rDepth + 1)


def height1(node):
    if (node is None):
        return 0
    else:
        return max(height(node.left),height(node.right))+1

t = int(input())
n = int(input())

arr = list(map(int,input().split()))

root  = Node(arr[0])

for i in range(1,n):
    root.insert(arr[i])

print(height1(root))