class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def insertData(self,data):
        temp = self.head
        x = temp
        while(temp.next):
            temp = temp.next
            x = temp
        temp = Node(data)
        x.next = temp

    def insertNumData(self,data,num):
        if num ==0:
            x = Node(data)
            x.next = self.head
            self.head = x
        else:
            temp = self.head
            for i in range(1,num):
                temp = temp.next

            x = Node(data)
            x.next = temp.next
            temp.next = x

    def dltData(self,data):
        temp = self.head
        if data == temp.data:
            self.head = temp.next
        else:
            while(data!=temp.next.data):
                temp = temp.next
            temp.next = temp.next.next

    def dltNumNode(self,num):
        if num==0:
            self.head = self.head.next
        else:
            temp = self.head
            for i in range(1,num):
                temp = temp.next
            temp.next = temp.next.next



if __name__=='__main__':
    llist = LinkedList()

    llist.head = Node(0)

    llist.insertData(1)
    llist.insertData(2)
    llist.insertData(3)
    llist.insertData(4)
    llist.insertData(5)
    llist.insertData(6)
    llist.insertData(7)
    llist.insertData(8)
    llist.printList()

    llist.insertNumData(23,2)
    llist.insertNumData(28,4)
    llist.insertNumData(33,6)
    llist.insertNumData(35,6)
    llist.insertNumData(75,0)
    llist.insertNumData(85,0)

    llist.printList()
    # llist.dltData(1)
    # llist.dltData(5)
    # llist.dltData(8)
    #
    # llist.printList()
    #
    print("_______")

    # llist.dltNumNode(5)
    # llist.printList()
    # print("________________")
    # llist.dltNumNode(0)
    # llist.printList()
    # print("________________")
    # llist.dltNumNode(2)
    # llist.printList()
    # print("________________")
    #
    # llist.dltNumNode(0)
    # llist.printList()
    # print("________________")
    # llist.dltNumNode(0)
    # llist.printList()
    # print("________________")