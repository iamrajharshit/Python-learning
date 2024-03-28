'''First person enters the line leaves the line
Process managment in OS.
'''
from node import Node

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def insert(self,value):
        inVal =Node(value,None)

        if self.size==0:
            self.front=inVal
            self.rear=inVal
        else:
            self.rear.setNext(inVal)
            self.rear = inVal

        self.size += 1    

    def remove(self):

        if self.size>0:
            val=self.front.getValue()
            self.front=self.front.getNext()
            
            self.size-=1
            return val
        else:
            return
        
    
    def display(self):
        if self.size<=0:
            print("queue empty")
            return
        else:
            curr=self.front
            while curr is not None:
                print(curr.getValue())
                curr=curr.getNext()
    

    def peek(self):
        return self.front.getValue()
    

    def size(self):
        return self.size