'''
Direct Recursion : When function calls itself.
Indirect Recursion : A function calls another function which calls the first function again.

'''

#Direct Recursion

'''
1) define a function take input
2) stopping condition
3) #statments #code 
4) recall with n-1 

'''

#Write a program for printing n to l seq

#n= int(input("Enter the value of n:"))
n=8
def  natural(n):
    if n==0:
        return
    print(n)
    return natural(n-1)

#Indirect Recursion

def num(n):
    if n<=0:
        return
    print(n,end=" ")
    return num1(n-1)

def num1(n):
    print(n,end=" ")
    return num(n-1)

#num(10)
