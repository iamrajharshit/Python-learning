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
print(find_vov(str1))    

###################################2#################################

'''
python prog to accept the strings which contains all vovles
'''

