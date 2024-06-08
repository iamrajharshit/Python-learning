'''
Maximun and min k element in tuple
'''
n=(34,67,121,573,567,35,7)
def max_min(n):
    return f'MAx: {max(n)} and Min: {min(n)}' 

#print(max_min(n))

#####################################2#################################

'''
create a list of tuple from given list having numbers
'''
l=[2344,56,34,575,23,673,4]
def list_to_tuple(l):
    t=tuple(l)
    return t
print(list_to_tuple(l))


########################################3#################################


'''
Adding tuple to list and vice-versa
'''
t=(23,45,67,8)

def add_tuple(t):
    for i in t:
        l.append(t)
    return l    

