# try:
#     a=[5,6,3,7,4,5]
#     print(a[3])

# finally:
#     print("End of project")


class InvalideAgesException(Exception):
    "Raise when the input value less than 18"
 

number=18
num=int(input("enter the number:"))
try:
    num=int(input("enter the number:"))
    if num < number:
        raise InvalideAgesException
    else:
        print("Eligibele to vote")
except InvalideAgesException:
    print("Age should be above 18 to vote")