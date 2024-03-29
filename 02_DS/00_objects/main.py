from Employee import Employee

emp1=Employee("Raksha","Bang.","D A","45000")

emp2=Employee("Preksha","Del","SDE","60000")

print(emp1.getName(),":",emp1.getSal())
print(emp2.getName(),":",emp2.getSal())
emp1.setJob("S D A")
emp1.setSal("65000")

print("After change",emp1.getName(),":",emp1.getSal())
