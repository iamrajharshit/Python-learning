'''
List Comprehension is faster then for loop and improves performance, a shorten way of writing code.
'''

#Syntax
''' 
[`expression` for `item` in `iterable`]

expression could be for dict k:v pair, just var for list

'''

# Examples
def list_comp1():
# Simple
    l=[]
    for i in 'python':
        l.append(i)
    print(l)

# list comp
    return [i for i in 'python']


print(list_comp1())

# to print only even numbers into the list
print([i for i in range(20) if i%2==0])


# nested codition like divisible by 2 and 3
print([i for i in range(20) if i%2==0 if i%3==0])


# using AND/ OR condition

print([i for i in range(20) if i%2==0 or i%3==0])
print([i for i in range(20) if i%2==0 and i%3==0])
print(['Even' if i%2==0 else 'Odd' for i in range(20)])






'''
Take a matrix as input and return a list with each row placed on after the other
'''

def list_comp():

# Non List Comp
    def flatMatFor(matrix):
        flat=[]
        for row in matrix:
            for i in row:
                flat.append(i)
        return flat
    matrix=[range(0,5), range(5,10), range(10,15)]
    print(matrix)
    print(flatMatFor(matrix))

#List comp
    def flatMatLc(matrix):
        return [x for row in matrix for x in row]
    print(flatMatLc(matrix))

list_comp()

'''
Take a string as input and return a string with vowels removed.
'''
def list_comp2():
#simple one
    def removeVow(input):
        vow='aeiou'
        f1=[]
        for i in input:
            if i not in vow:
                f1.append(i)

        return ''.join(f1)
    input="python is simple to learn"
    print(removeVow(input))

#list comped
    print(''.join([i for i in input if i not in 'aeiou']))

list_comp2()