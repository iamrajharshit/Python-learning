#will use node object to make the stack
from node import Node
class Stack:
    
    def __init__(self):
        self.top = None #none type

    #Push passing element 
    def push(self,value):
        newnode=Node(value,self.top) #we are creating a new node, with the user value, pointing the current top.
        #self.top becomes a reference to that node
        #now update the top
        self.top=newnode #now top is pointing to the current node (newnode is the var for new node) 
        #here top datatype is changed to node (can access value and next)

    #Pop
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
   
    #peek    
    def peek(self):
        #to know thats on the top of the stack
        return self.top.getValue()

    #display
    def display(self):
        #making a pointer or variable which will act same as top
        current = self.top
        #as will be traverse to the last node, we have a loop
        while current is not None:
            #to print only values else none will be printed! ref. init top was none
            if current.getValue() is not None:
                return(current.getValue()) #to print vlaues
            current = current.getNext() #to move forward in the stack using the -> next node 


    #isEmpty
    def isEmpty(self):
        return self.top is None #(True if its none else false)