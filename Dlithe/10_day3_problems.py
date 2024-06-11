
def to_roman(num):
    rom_dic={'I':'1','v':'5','X':'10','l':'50','C':'100','D':'500','M':'1000'}
    for n in num:
        for k, v in rom_dic.items():
            if n in v:
                return k
        

# print(to_roman('1'))





'''
Input: IX
Output: 9
IX is a Roman symbols which reps 9

Input: XL
Output: 40

'''

def to_num(rom):
    rom_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for chr in rom:
        for k,v in rom_dict.items():
            if chr in k:
                return v
            

#print(to_num("L"))

#################################################2#################################

'''
Prog to solve classic ancient chinese puzzle we count 35 heads and 94 legs among the chickens and 
rabbits in a farm how many rabbits and how many chickens do we have?
'''
import numpy as np
from scipy.linalg import solve

def find_chick_rab(heads,legs):

    # Define the system of equations (Ax = b)
    A = np.array([[1, 2], [1, 4]])  # 1 head and 2 legs for chicken, 1 head and 4 legs for rabbit
    B = np.array([heads, legs]) 
    print(A)
    print(B)
    result=solve(A,B)
    chickens, rabbits = result
    # print("Number of chickens:", chickens)
    # print("Number of rabbits:", rabbits)
    
    return f"Number of chickens: {chickens}and rabbits: {rabbits}"

#print(find_chick_rab(5,14))

def find(head,legs):
    rabs= legs/2-head
    chick=head-rabs
    return f"Number of chickens: {chick}and rabbits: {rabs}"

#print(find(35,94))

################################################4##################################################

'''
a ROBOT IN A PLANE  STARTING FROM ORIgin point(0,0) The robot can move towards UP, DOWN,LEFT, RIGHT with a given
steps 
UP 5 
DOWN 3
LEFT 3
RIGHT 2
Program to compute the distance from current position after a seq of movement and original point.
'''
import math 
from math import sqrt
def move_robo():
    moves=int(input("Enter number of moves:"))
    mvts=[]
    print(mvts)
    for i in range(moves):
        key=input("Enter UP/DOWN/LEFT/RIGHT")
        step=int(input("Enter the value:"))
        mvts.append((key,step))
    print(mvts)

    def distance(mvts):
        x_p=0
        y_p=0
        for k,v in mvts:
            if k =="UP":
                y_p=y_p+v
            if k =="DOWN":
                y_p=y_p-v
            if k=="LEFT":
                x_p=x_p-v
            if k=="RIGHT":
                x_p=x_p+v

        return f"distance= {sqrt((x_p**2)+(y_p**2))}"
    
    return distance(mvts)

#print(move_robo())



#print(move_robo())

################################################################5#######################################

'''
Stock buy and sell to maximize profit

input: [100,180,260,310,40,535,695]
output: -100+310-40+695

'''
def profit():
    pass

#####################################################6####################################################

'''
Possible combination elements
input: [1,2,3]
output: [1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]
'''
from itertools import combinations

l=[1,2,3]
def to_find_combi(l):
    list_combi=[]
    for i in range(len(l)+1):
        combi=combinations(l,i)
        list_combi.extend(combi)

    return (list_combi)

#print(to_find_combi(l))

########################################################7##################################################

"""
sorting boundry elements in matrix 

1 2 3 4 0 
1 1 1 1 2 
1 2 2 2 4 
1 9 3 1 7

output:

 0 1 1 1 1 
 9 1 1 1 1 
 7 2 2 2 2 
 4 4 3 3 2 

"""
# import numpy as np
# input=np.array([[1,2,3,4,0],[1,1,1,1,2],[1,2,2,2,4],[1,9,3,1,7]])

# sorted_matrix = input[input[:, 0].argsort()]
# print(sorted_matrix)


input_mat=[
    [1,2,3,4,0],[1,1,1,1,2,],[1,2,2,2,4],[1,9,3,1,7]
]
boundary_elements=[]
boundary_indx=[]

for idx1, j in enumerate(input_mat):
    print(idx1,'->',j,"x")
    for ind2, k in enumerate(j):
        print(ind2,'->',k)


####################################################8##############################################################
'''
input: 2004 S=2

Output: 1999
'''
yearx='2004'
removex=2
def nearest_year(yearx,removex):
    pass

def NotPresent(i,s):
    temp= int(s)
    while i:
        digit=i%10
        i=i//10
        t=temp
        while t:
            digit2=t%10
            t=t//10
            if digit2==digit:
                return False
            
    return True

def grn(n,s):
    N=int(n)

###################################################################9#####################################################
