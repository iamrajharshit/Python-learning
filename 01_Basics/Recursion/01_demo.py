'''
When a function calls itself, then that function is called as recursive function and process is called as recursion.
In recursion, the function is called inside itself with change in the parameters.
'''

import sys
# Recursion error 1000 is the limit, it can be checked
print(sys.getrecursionlimit())
#to set limits
sys.setrecursionlimit(200)
i=0
def demo():
    global i
    print("hello")
    # i=i+1
    # print(i)
    return demo()
   
demo()

#clean code
#can solve complex problems

#also hard to debug
#not memory efficient