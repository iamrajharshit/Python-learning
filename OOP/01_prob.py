"""Define a class named "Employee" with fields em_id, name, dep_id, blood_group and salary.
Declare two public method get and set thee fields.
Create an array / list of employee object prompt the user for providing values and 
show the details pf emp on the std output.
"""

class Employee:
    
    dep_id=0
    blood_group="A"
    salary=5000

    def __init__(self,id,name):
        self.emp_id=id
        self.emp_name=name
    
    def setFields(self):
        dep_id=int(input("Enter the dep_id"))
        self.dep_id=dep_id

        blood_group=input("Enter the blood group")
        self.blood_group=blood_group

        sal=int(input("Enter the salary"))
        self.salary=sal

    def getFields(self):
        return f"EmpID:{self.emp_id}\tName:{self.emp_name}\tDepID:{self.dep_id}\tBloodGroup:{self.blood_group}\tSalary:{self.salary}"

    def __str__(self):
        return str(self.emp_name)
    def __repr__(self):
        return str(self.emp_name)


# emp1=Employee("001","Harshit")
# emp1.setFields()
# print(emp1.getFields())

Emp_list=[]
# Emp_list.append(emp1)


num_emp=int(input("Enter the number of emp to be added:"))

for i in range(num_emp):
    emp_id=input("Enter the emp_id")
    emp_name=input("Enter the emp name:")
    emp=Employee(emp_id,emp_name)
    emp.setFields()
    Emp_list.append(emp)

print(Emp_list)
