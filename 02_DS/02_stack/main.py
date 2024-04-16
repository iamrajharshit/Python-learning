#stack implementation
#Last in First Out
#push, pop, stack-empty, stack-full

'''Stack is a memory managment. 
Each of these entries of the stacks are nodes, we have to keep track of which one is on top of the stack
and that one will point to the next value of the stack, bellow it. '''

# considering a stack (top) 3->4->5->(none) (last)

#Implementation
#will use node object to make the stack under stack.py

from stack import Stack

s=Stack()

s.push(4)
s.push(5)
# s.push(3)
# s.push(4)

# print(s.pop())
# print(s.pop())

