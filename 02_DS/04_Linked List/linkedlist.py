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
      prevNODE.setNext(newNode)
      newNode.setNext(currNODE)
    self.size+=1

  def remove(self,indx):
    if indx > self.size:
      print("Index out of range")

    elif indx==0:
      self.front=self.front.getNext()

    else:
      i=0
      preNODE=self.front
      currNODE=self.front
      while i<indx:
        preNODE=currNODE
        currNODE=currNODE.getNext()
        i+=1

      preNODE.setNext(currNODE.getNext())
      currNODE.setNext(None)
    self.size-=1


  def __str__(self): #overriding a method
    strRet =""
    #new node pointer name holder
    holder=self.front

    #moving till the last node
    while holder is not None: 
      strRet+=str(holder.getValue())
      holder=holder.getNext()

    return strRet

  def __getiem__(self,item):
    if item > self.size:
      print("Index out of bounds")

    else:
      i=0
      holder = self.front

      while i!=item:
        holder=holder.getNext()
        i+=1

    return holder.getValue()
  
  def __len__(self):
    return self.size


       


           

           


          

    
          


    
