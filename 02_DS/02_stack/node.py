'''A fundamental DS that holds two pieces of info, holds the value of the cureent node and the pointer to the next thing that follows it (next value it in stack or value in queue)
In py we keep track the first thing in the list, when we iterate through the list we can just simply follow the next links unlit we reach the end. (value and the link to next)
'''

#implimentation
class Node:
    def __init__(self, value,next):
        self.value = value
        self.next = next
        
    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.next
    

    def setValue(self,value):
        self.value=value

    def setNext(self,next):
        self.next=next

    def __str__(self):
        return str(self.value)
    