#stack implementation
#Last In First Out #First In Last Out
#push, pop, display, stack-empty, stack-full

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

print("After Push")
s.display()
print(f"Lets pop top element or node: {s.pop()}")

print("lets look into our stack")
s.display()

print(f"Is our stack empty?\n{s.isEmpty()}")

print(f"whats on top?\n{s.peek()}")
