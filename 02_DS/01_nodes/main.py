from node import Node

# 4->3->none

f=Node(3,None)

s=Node(4,f)

f.setNext(s)
s.setValue(8)

print(s.getValue(),"-->",s.getNext(),"-->",f.getNext())


