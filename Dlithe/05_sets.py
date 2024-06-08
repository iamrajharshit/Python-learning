'''
count vovels using sets in given string.
'''
str1="I am raj harshit who are you?"

def find_vov(str1):
    c=0
    for i in str1.lower():
        if i in {'a','e','i','o','u'}:
            c=c+1
    return c        
#print(find_vov(str1))    

###################################2#################################

'''
python prog to accept the strings which contains all vovles
'''
str2= "I am Raj you knew it right"

def all_vov(str2):
    for i in {'a','e','i','o','u'}:
        if i in str2.lower():

            return True
        else:
            return False

print(all_vov(str2))


#########################################3###########################

'''concatenated string with uncommon char in python'''

s1="aabd"
s2="dgh"

def concat_at_com_char(s1,s2):
    s_new=" "
    for chr in s1:
        if chr not in s2:
            s_new= s_new + chr

    for char in s2:
        if char not in s1:
            s_new= s_new+char

    return s_new


a={1,1,2,3}
b={3,4,5,6}

#union operation
print(a|b)
print(a.union(b))

#intersection
print(a&b)
print(a.intersection(b))

#difference
print(a-b)
print(a.difference(b))

print(a^b)

print(a==b)
