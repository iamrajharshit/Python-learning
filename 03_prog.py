# square_gen=(i*i for i in range(5))
# for k in square_gen:
#     print(k)



lst=[1,2,5,3,57,11]
new_list=list(filter(lambda x: (x%2==0),lst))
#print(new_list)    


#clourse
def greet(name):
    def disp_name():
        print(name)

    disp_name()
greet("Avi")


#Decorator
def add(x,y):
    return x+y

def mul(x,u):
    return x*u

def cal(func,x,y):
    return func(x,y)

result= cal(mul,4,6)
print(result)

