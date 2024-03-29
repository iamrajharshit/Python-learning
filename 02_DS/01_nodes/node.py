'''A fundamental DS that holds two pieces of info, holds the value of the cureent node and 
the pointer to the next thing that follows it (next value it in stack or value in queue)
In py we keep track the first thing in the list, when we iterate through the list we can
 just simply follow the next links unlit we reach the end. (value and the link to next)
'''

#Implimentation
#class name same as our file
class Node:
    # will initialize with a value and a next pointer
    def __init__(self, value,next):
        self.value = value #to hold the value 
        self.next = next   # to hold the address of the next node in next pointer
        
    def getValue(self):
        return self.value #to get the value of the node 
    
    def getNext(self):
        return self.next # to get the address of the node
    

    def setValue(self,value):
        self.value=value # to set the value 

    def setNext(self,next): 
        self.next=next # to set the next pointer

    def __str__(self): #__str__ to convert integer to a string for instance (here, it will convert a node into text)
        return str(self.value) #to print node object (next) "getNext().getValue()"
    