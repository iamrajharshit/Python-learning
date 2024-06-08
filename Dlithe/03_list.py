#prog to print even numbers

def print_even_nums(nums):
  
  for num in nums:
    if num % 2 == 0:
      print(num)
nums=[1,3,5,6,3,5,7,8]
#print(print_even_nums(nums))

#########################################2############################

'''
find the sec largest element in list.
''' 

def secLar(l):
  if len(l)<2:
    return None
  else:
    l.sort(reverse=True)
    return l[1]
l=[34,23,54,2,56,4]  
#print(secLar(l))  


def find_secLag(numbers):

  largest = secLag = float('-inf') 

  for num in numbers:
    
    if num > largest:
      secLag = largest
      largest = num
    elif num > secLag and num != largest:
      secLag = num

  return secLag

#print(find_secLag(l))

########################3#########################################

'''
Break a list into chunks
'''

l=[1,3,4,5,6,7,9]
def breakin(n,l):
  x=len(l)//n
  for i in range(x):
    print(l[i*n:(i+1)*n])


print(breakin(3,l))
  
  
###############################4###################################


