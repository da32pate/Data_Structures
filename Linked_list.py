class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
     self.head = None

    # add at the start of LL 
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # add at the last of LL 
    def add_last(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            n = self.head
            while(n.ref is not None):
                n = n.ref
            n.ref = new_node

    #insert node after a node on a LL
    def add_after(self, x, y):
        new_node = Node(y)
        n = self.head
        while(n is not None):
            if (n.data == x):
                new_node.ref = n.ref
                n.ref = new_node
                return
            n = n.ref
        if(n == None):
            print("Cannot add after bcz no number found")
            return
            
        
                
    #delete a node from begininng
    def delete_begin(self):
        if self.head == None:
            print("LL is empty cant delete")
        else:
            self.head = self.head.ref

    #delete a node from end
    def delete_end(self):
        if self.head == None:
            print("LL is empty cant delete from end")
        else:
            # n = self.head
            if self.head.ref.ref is None:
                self.head.ref = None

    #delete a node having a particular value
    def delete_by_value(self, x):
        if self.head == None:
            print("LL is empty cannot delete by value")
            return
        else:
            if self.head.data == x:
                self.head = self.head.ref
                return
        n = self.head
        while(n.ref is not None):
            if n.ref.data ==x:
                n.ref = n.ref.ref
                return
            n = n.ref
        if n.ref is None:
            print("the value is not present in LL")
            return
                   
    #Traversing a LL
    def print_ll(self):
        if self.head == None: 
            print("LL is empty")
        else:
            n = self.head
            while(n is not None):
                print(n.data)
                n = n.ref
    

obj = LinkedList()
obj.add_last(10)
obj.add_last(20)
obj.add_last(30)
obj.add_after(20,15)
obj.print_ll()


