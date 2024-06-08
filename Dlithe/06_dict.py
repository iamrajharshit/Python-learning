# dict1={1:"raj",2:"Rahul",3:"Rohan"}

# print(dict1.get(3))

# my_dict = {"name": "Alice", "city": "New York"}
# del my_dict["city"]  # Removes the key-value pair with key "city"
# print(my_dict)

dict1={}

for i in ["i","raj","i","df"]:
    dict1[i]=dict1.get(i,0)+1

#print(dict1)

##########################1###############################################

'''Write a python prog to check the validity od a pass'''








##########################################2################################
'''check for url in a string'''
import re
str1="iamrajharshit@gmail.com, shreyasgunaje@gmail.com fsdf ijfiwenfi   rajharshit388@gmail.com.....efjiowj eifjj "
emails=re.findall("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]+",str1)
print(emails)

###########################################3###############################

