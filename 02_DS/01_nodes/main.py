from node import Node

# 4->3->none

first =Node(3,None) #its like end
print(first.getValue(),"-->",first.getNext())
Sec=Node(4,first)

print(Sec.getValue(),"-->",Sec.getNext())

third=Node(7,Sec)

print(third.getValue(),"-->",third.getNext())