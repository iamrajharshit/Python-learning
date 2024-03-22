from node import Node

# 4->3->none

first =Node(3,None) #its like end
Sec=Node(4,first)

print(Sec.getNext(),Sec.getValue())