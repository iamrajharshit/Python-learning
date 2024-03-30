'''
Objects and Classes are sort of like a gen. programming concepts
its a way of representing data in our programming languages.

Example: Employee
Employee has attributes, properties associated with it.
-name
-location 
-job title
-salary
our goal would be to represent all of the data in a single entity.

With object, we can represent all of this (attributes) in a single object.

defining methods helps us to interact us with the properties. 

A class, we are going to call it, what we want to call our object.
(In gen. we name the class same as the file name.)
Object is a single instance of a Class.
'''
class Employee:

    def __init__(self, name, loc, job,sal):
        self.name=name
        self.loc=loc
        self.job=job
        self.sal=sal

    def getName(self):
        return self.name
    
    def getLoc(self):
        return self.loc
    
    def getJob(self):
        return self.job
    
    def getSal(self):
        return self.sal 
    
    def setName(self,name):
        self.name=name

    def setLoc(self,loc):
        self.loc=loc

    def setJob(self,job):
        self.job=job

    def setSal(self,sal):
        self.sal=sal


