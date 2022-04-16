#3! (1x2x3)
#5! (1x2x3x4x5)

num= int(input("number:"))
factorial=1

if num<0:
    print("number must be +ve")
elif num==0:
    print("factorial = 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
print(factorial)    

