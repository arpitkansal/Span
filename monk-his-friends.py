class Node:
    def __init__(self, data):
        self.data = data
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

    def search(self, x):
        if x == self.data:
            print("YES")
        elif x > self.data:
            if self.right is None:
                self.right = Node(x)
                print("NO")
            else:
                self.right.search(x)
        elif x < self.data:
            if self.left is None:
                self.left = Node(x)
                print("NO")
            else:
                self.left.search(x)


t = int(input())
while (t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    root = Node(arr[0])
    for i in range(1, n):
        root.insert(arr[i])
    for i in range(n, n + m):
        root.search(arr[i])
    t -= 1