#declaration of class
class Student:
    #class variable --> shared among all instances of class
    no_of_students=0
    #instance variable--> unique for each element
    fees=50000

    #similar to CONSTRUCTOR -->__init__
    #self-->this
    def __init__(self,name,surname,city,age):
        self.name=name          #this.name=name
        self.surname=surname
        self.age=age
        self.city=city
        Student.no_of_students+=1

    def details(self):
        return '{} {} {} {}'.format(self.name,self.surname,"from",self.city)

    def add(self,a,b):
        sum=a+b
        return sum
    def StudFees(self):
        f=int(input("Enter fee concession percent:"))
        self.fees=self.fees-(f*self.fees/100)


#creating instance --> Creating object of class (along with constructor)
print("------------------------")
print(Student.no_of_students)
S1=Student('Baburao','Apte','Chicago',20)
S2=Student('Harshad','Mehta','Mumbai',18)
print(Student.no_of_students)
print("------------------------")

#changes for entire class and instances
Student.fees=60000

#changes only for given instances
S1.fees=70000

#S1 is passed implicitely as first paramater
print("------------------------")
#calling a function:
#1)using class name and instance as parameter
print(Student.details(S1))
#2)directly using instance and method ( similar to java )
print(S1.details())
print(S2.details())
print("------------------------")

#sample method
print(S1.add(5,10))
print(S2.add(25,19))
print("------------------------")

#fees attribute is checked first for class and then istances
print(Student.fees)
print(S1.fees)
print(S2.fees)
print("------------------------")

#method below will change the 'fees' value for S2 using method(not like assigning value line 40)
S2.StudFees()
print(S2.fees)
print(S1.name+" age is:"+str(S1.age))
print(S2.name+" age is:"+str(S2.age))
print("------------------------")

#namespaces of class and instance
print(S1.__dict__)
print(S2.__dict__)
print(Student.__dict__)
print("------------------------")
