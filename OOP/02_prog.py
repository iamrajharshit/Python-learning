from abc import ABC,abstractclassmethod

class Car(ABC):

    def __init__(self,brand):

        self.brand=brand

    @abstractclassmethod
    def printDetails(self):
        pass


class Hatchback(Car):
    def printDetails(self):
        print(self.brand)


car1=Hatchback("Hyndai")
car1.printDetails()


class Ponit:

    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self) -> str:
        return "((0),(1))".format(self.x,self.y)
    
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y

        

