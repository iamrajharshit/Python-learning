'''Check if a given key exists in a dict or not
'''
def check_key():
    d={"Suresh":566,"Ramesh":567,"Kishore":490,"John":590}
    user_ip = input("enter the key to be verified:")
    if user_ip in d.keys():
        print("Key is there")
    else:
        print("Key not found!")

# check_key()


"""
Concate two dict into one dict like append
"""
def concat():
    d1={"Suresh":566,"Ramesh":567,"Kishore":490,"John":590}
    d2={"Swani":567,"Saachi":61,"Zihab":49}
    d1.update(d2)
    print(d1)

# concat()

"""Miultiply all the values in a give dict
"""
def multiply():
    d={'a':23,'b':56,'c':367,'d':678}
    m_value = 1
    for i in d:
        m_value = m_value*d[i]
    print(m_value)

# multiply()

'''
Calculate sum of all values in a dict
'''
def sum_of_val():
    d={"Suresh":566,"Ramesh":567,"Kishore":490,"John":590}
    total = sum(d.values())

    print(total)

# sum_of_val()


''' Convert two lists into a dict
'''
def convert_2L_to_dict():

    k=['a','b','c','d','e']
    v=[1,2,3,4,5]

    d=dict(zip(k,v))
    # it creates a tuple ('a','A')...

    print(d)

# convert_2L_to_dict()

'''Count the frequency of words appearing in a string
'''
def words_and_count():
    user_str=input("Enter string")
    l=user_str.strip() #char wise
    l=user_str.split() #word wise
    d={}
    for i in l:
        #now we need to store every word as a key into the dict
        #count as a value
        # if i not in d.keys(): #to check if key exists
        #     d[i]=0 # if not add it
        # d[i]=d[i]+1 # else increment it
        d[i]=d.get(i,0)+1 #works same
    print(d)

# words_and_count()

'''
create a dict which contains num btw 1 to n as a key 
and sqr of them as a value
'''
def num_sqr():
    n=int(input("Enter n value:"))
    d= {i:i**2 for i in range(1,n+1)}
    print(d)

# num_sqr()

'''
Create a dict from list og striings where the first char 
act as key and resp strings are stored as values.
'''

def str_key_val():
    user_str=input("Enter string: ")
    words=user_str.split()
    d={}
    for strr in words:
        ch=strr[0]
        if ch not in d:
            d[ch]=[]
            d[ch].append(strr)

    print(d)

    for k,v in d.items():
        print(k,':',v)

# str_key_val()


'''
List comprehension | Dict comp
'''
def comp():
    def dictCompFor(keys,values):
        d={}
        for i in range(len(keys)):
            d[keys[i]]= values[i]
        return d
    
    keys=[1,2,3,4,5]
    values=['one','two','three','four','five']
    print(dictCompFor(keys,values))

    #comp

    def decCompDc(keys,values):
        return {keys[i]:values[i] for i in range(len(keys))}
    
    print(decCompDc(keys,values))


comp()





