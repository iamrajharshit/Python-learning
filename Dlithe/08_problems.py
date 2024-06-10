# Chocolate distribution program
l=[7,3,2,4,9,12,36]
m=3
def minn_val(l,m):
    l.sort()
    # print(l)
    # print(l[:-m+1])
    diff=[]
    for i,n in enumerate(l[:-m+1]):
        # print(i,'->',n)
        d=l[i+m-1]-n
        diff.append(d)
    min_indx=diff.index(min(diff))
    return l[min_indx:min_indx+m]


# print(minn_val(l,m))


###############################################2##################################

l2=[2,4,6,8]

def val(l2):
    map={}
    for i in range(1,max(l2)+1):
        count=0 
        for j in l2:
            if j%i==0:
                count+=1
        map[i]=count 
    print(map)

print(val(l2))

#############################################3#######################################

"""

distribution problems
""" 
def distri():
    pass

