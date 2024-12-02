# a=int(input("Enter a value:"))
# b=int(input("Enter value b:"))

def findLCM(a,b):
    l=a if a>b else b
    while(l<=a*b):
        if l%a==0 and l%b==0:
            print("LCM is",l)
            break
        l+=1
    return l

# print(findLCM(a,b))

###########################@###############

l1=[45,67,89]
a,b,c = l1
# print(a,b,c)

l2=a,c,b
print(l2)
print(type(l2))
l3=[]
l3=b,a,c
print(l3)

