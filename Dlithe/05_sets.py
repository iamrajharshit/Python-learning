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

'''

'''