from node import Node

# 4->3->none

first =Node(3,None) #its like end
sec=Node(4,first)

print(sec.getNext(),sec.getValue())