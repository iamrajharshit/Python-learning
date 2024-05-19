#Python Input Handling
"""Lets say based on input we want to call a function"""

#will use match function()

def do_add():
    print("this function adds numbers")


def do_sub():
    print("This function substracts numbers")

match input("Add or Subtract"):
    case "Add":
        do_add()

    case "Subtract":
        do_sub()

    case _: #default
        print("invalid input")
