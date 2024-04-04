from node import Node

class Linked:
    
    def __init__(self):
      self.size=0   #to keep track of the size of the LL
      self.front=None

    #to insert at a given indx we pass index
    def insert(self, indx, value):
        newNode= Node(value,None)

        if indx > self.size:
          print("Index out of range")

        #we take the new node and we're going to set its next value to be what is at the front of the LL
        elif indx ==0:
           newNode.setNext(self.front)
           self.front=newNode #base case

        else:
           i=0 #index i which is zero
           #will keep track of the current node
           currNODE=self.front
           prevNODE=self.front

           while i<indx:
              prevNODE=currNODE
              currNODE=currNODE.getNext()
              i+=1

           newNode.setNext(currNODE)
           prevNODE.setNext(newNode)
        
        self.size+=1

           


          

    
          


    
