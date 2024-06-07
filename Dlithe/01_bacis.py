'''
Python program for factorial of a number 
'''

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
#print(fact(6))
# from math import factorial
# print(factorial(7))

###################################################2############################

def ascii(char):
    return ord(char)

# print(ascii('a'))

###########################################3#####################################

def sum_0f_n(num):
    c=0
    for i in range(1,num+1):
        c=c+(i*2)
    print(c)
# print(sum_0f_n(10))
    
#########################################4########################################
'''
11111
10001
10001
11111
'''

def pattern(p):
    i=p
    while(i!=0):
        if i==p:
            print('1'*(p))
        elif i==1:
            print('1'*(p))        
        else:
            print("1"+"0"*(p-2)+"1")   
        i=i-1


# print(pattern(4))        

###########################################################5###########################

'''
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''

def pascal_t(n):

    for i in range(1,n+1):
        for j in range(i):
            print('1',end="")

        print('\n')
        

#print(pascal_t(2))

def pascal(n):

    for i in range(1,n+1):

        for j in range(0,n-i+1):
            print(" ",end='')
            c=1
        print("\n")    
        for j in range(1,i+1):
            print(" ",c,end="")
    
            c=c*(i-j)  # for pascal's triangle

print(pascal(5))


    
             
                   


