"""
Basic template
def defname(parameters):
    if base condtions:
        return
    code
    return [recursion call]
"""


def fact(n):
    if n==0:
        return 1 #as fact(0) is 1, it also stops the rec
    return n * fact(n-1) #final stored output is returned
    
print(fact(5)) 

#5! =5*4*3*2*1 = 120
'''
Stack push
fact(5) * (5-1)
fact(4) * (4-1)
fact(3) * (3-1)
fact(2) * (2-1)
fact(1) * (1-1)
'''
""" 
When the function reaches n=0, it stops recursion and 
starts returning values back up the call stack.
"""
'''
When fact(0) is reached it returns 1 base case (n==0)
Stack pop
fact(1) * 1 (returned from fact(0)) = 1 ; n=1
fact(2) * 1 (returned from fact(1)) = 2 ; n=2
fact(3) * 2 (returned from fact(2)) = 6 ; n=6
fact(4) * 6 (returned from fact(3)) = 24 ; n=24
fact(5) * 24 (returned from fact(4)) = 120 ; n=120
'''
#returned 120