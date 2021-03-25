#super/parent class
class Student:

    #instance variable--> unique for each element
    fees=50000
    age=8
    def __init__(self,name,surname,age):
        self.name=name          #this.name=name
        self.surname=surname
        self.age=age

    @staticmethod
    def add(a,b):
        return a+b


#sub-class declaration syntax
class Primary(Student):
    age=10

    def __init__(self,name,surname,age,std):
        #super method will inherit the init function from super class student
        super().__init__(name,surname,age)
        self.std=std

    @staticmethod
    def add(a,b):
        return 2*(a+b)
class Secondary(Student):
    age=14

    def __init__(self,name,surname,age,sub):
        super().__init__(name,surname,age)
        self.sub=sub

    @staticmethod
    def add(a,b):
        return 3*(a+b)

#S0 will take 4 arguments(1 default)
S0=Student('abc','xyz',8)
#S1 will take 5 arguments(1 default)
S1=Primary('abc','xyz',15,8)
#S2 will take 5 arguments(1 default)
S2=Secondary('efg','pqr',20,'economics')

print("-------------")
print(S0.age)
print(S1.age)
print(S2.age)
print("-------------")
#extra variables in input
print(S1.std)
print(S2.sub)
print("-------------")
#print(help(Student))

#"isinstance" instell if any object is instance of class --> returns true for super and sub class, false if not
print(isinstance(S1,Student))
print(isinstance(S1,Primary))
print(isinstance(S1,Secondary))     #returns false
print("-------------")

#"issubclass" instell if any class is sub class of another class--> returns true if subclass present else false
print(issubclass(Primary,Student))
print(issubclass(Secondary,Student))
print(issubclass(Primary,Secondary))
print("-------------")

#Example for METHOD OVERRIDING
print(S0.add(5,10))
print(S1.add(5,10))
print(S2.add(5,10))
print("-------------")
