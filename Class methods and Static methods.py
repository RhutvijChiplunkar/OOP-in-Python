#declaration of class
class Student:

    #instance variable--> unique for each element
    fees=50000

    #similar to CONSTRUCTOR -->__init__
    #self-->this
    def __init__(self,name,surname,city,age):
        self.name=name          #this.name=name
        self.surname=surname
        self.age=age
        self.city=city


    #CLASS METHOD decorator
    @classmethod
    #It has parameter as class. all the changes here are done with respect to class
    def change_fees(cls,amount):
        cls.fees=amount

    #In this method we will pass string and will return it as an instance
    @classmethod
    def fromString(cls,stud_str):
        name,surname,city,age=stud_str.split('-')
        return cls(name,surname,city,age)

    #STATIC METHODS --> self or cls parameter is not passed by default. It is any general method in class
    #static method decorator
    @staticmethod
    def percent(total):
        return total/5.0

S1=Student('Baburao','Apte','Chicago',20)
S2=Student('Harshad','Mehta','Mumbai',18)

print("-----------------")
print("OLD FEES")
print(Student.fees)
print(S1.fees)
print(S2.fees)
print("-----------------")

#calling class method
Student.change_fees(60000)
print("-----------------")
print("NEW FEES")
print(Student.fees)
print(S1.fees)
print(S2.fees)
print("-----------------")

#input for "fromString" method
stud_str1="Virat-Kohli-Delhi-31"
stud_str2="Rohit-Sharma-Mumbai-35"

#call "fromString" method
stud1=Student.fromString(stud_str1)
stud2=Student.fromString(stud_str2)

print(stud1.city)
print(stud2.city)
print("-----------------")

#call the static method --> can be done by class as well as instances
print(Student.percent(500))
print(stud1.percent(350))
print(stud2.percent(269))
print("-----------------")
