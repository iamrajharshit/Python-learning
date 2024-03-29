'''
Objects and Classes are sort of like a gen. programming concepts
its a way of representing data in our programming languages.

Example: Employee
Employee has attributes, properties associated with it.
-name 
-age
-salary
-job title
our goal would be to represent all of the data in a single entity.

With object, we can represent all of this (attributes) in a single object.

defining methods helps us to interact us with the properties. 

A class, we are going to call it, what we want to call our object.
(In gen. we name the class same as the file name.)
Object is a single instance of a Class.
'''

class Employee:
    
    def __init__(self,name,jobtitle,salary):
        self.name = name
        self.jobtitle = jobtitle
        self.salary = salary
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name=name
    
    def getSalary(self):
        return self.salary
    
    def setSalary(self,salary):
        if salary>0:
            self.salary=salary
        else:
            print("Salary must be greater than 0")
        return self.salary    

    def getJobtitle(self):
        return self.jobtitle
    
    def setJobtitle(self,jobtitle):
        self.jobtitle=jobtitle         


