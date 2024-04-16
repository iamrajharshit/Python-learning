#will use node object to make the stack
from node import Node
class Stack:
    
    def __init__(self):
        self.top = None #none type

    def push(self,value):
        inVal=Node(value,self.top) #we are creating a new node, with the user value, pointing the current top.
       # slef.top becomes a reference to that node
        #now update the top
        self.top=inVal #now top is pointing to the current node (inVal is the var for new node) 

    #now pop
    def pop(self):
        #first check if theres is anything in the stack
        if self.top is None:
            return 
        else:
            #store the value using getValue() defined in the node of the top node
            valRet=self.top.getValue()
            #get the next node value
            nextVal=self.top.getNext()
            #point the top to the nextVal
            self.top=nextVal
            #return that valRet
            return valRet
        
    def peek(self):
        #to know thats on the top of the stack
        return self.top.getValue()


    def display(self):
        current = self.top
        while current is not None:
            if current.getValue() is not None:
                print(current.getValue())
            current = current.getNext()


    
    def isEmpty(self):
        return self.top is None #(True if its none else false)