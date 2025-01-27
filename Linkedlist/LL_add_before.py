class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None


    def printLL(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,end=' ')
                n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head = new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head 
            while n.ref is not None:
                n=n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print('list is empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref=self.head
            self.head = new_node
            return
        
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n=n.ref

        if n is None:
            print('not found!')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node


ll1=LinkedList()                        
ll1.add_begin(13)
ll1.add_begin(14)
ll1.add_end(1000)
ll1.add_end(10)
ll1.add_begin(15)
ll1.add_begin(16)
ll1.add_before(7,10)
ll1.printLL()