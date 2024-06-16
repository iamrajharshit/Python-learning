# num=int(input("Enter the num of rows"))

def right_tri(num):
    for i in range(num):
        for j in range(i+1):
            print("*", end="")
    
        print()

# print(right_tri(3))        

def three_space(num):
    k=1
    for i in range(1,num+1):
        for j in range(1,k+1):
            print("*",end="")
        k=k+2
        print()

# print(three_space(3))

def pyramid(num):
    for i in range(0,num):
        pass
        
