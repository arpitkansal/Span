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

#n = int(input())
n = 5
#arr = list(map(int,input().split()))
arr = [4,7,8,6,3]
#val1, val2 = map(int,input().split())
val1, val2 = 7,6
root  = Node(arr[0])

for i in range(1,n):
    root.insert(arr[i])

#find lca

def lca(node,val1,val2):
    if node is None:
        return None
    if node.data > val1 and node.data>val2:
        return lca(node.left,val1,val2)
    if node.data < val1 and node.data < val2:
        return lca(node.right, val1, val2)
    return node

lca_node = lca(root,val1,val2)

grtr_num = max(val1,val2)

#print(lca_node.data)
def max_num(node,grtr_num):
    if node is None:
        return None
    if node.data == grtr_num:
        return node.data
    if grtr_num == node.right.data:
        return node.right.data
    if node.right:
        if grtr_num>node.right.data:
            return max_num(node.right,grtr_num)
        return node.right.data
    return node.data

grtst_num = max_num(lca_node,grtr_num)

print(grtst_num)