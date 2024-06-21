class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        self.prev = None
        
class List:
    
    def __init__(self):
        self.head=Node(None)
        self.head.next= self.head
        self.head.prev= self.head
        
        
        
    def get(self,index):
        
        if index >= self.size():
            raise Exception('out of list')
        x =self.head.next       
        for i in range(index):
            x=x.next
        return x
    
    
    def insert_last(self,x,data):
        
        y = Node(data)
        self.n+=1
        y.prev=x
        y.next=x.next
        x.next=y
        y.next.prev=y
        return y
    
    
    def remove(self,x):
        
        if self.size() == 0:
            raise Exception('List is empty')
        self.n -= 1
        x.prev.next = x.next
        x.next.prev = x.prev
        return x
    
    
    
    def find(self,value):
        
        x = self.head.next
        for i in range(self.size()):
            if x.data == value :
                return x
            x = x.next 
        return None
    
    
    
    def size(self):
        return self.n
    
    def is_empty(self):
        return self.n==0    