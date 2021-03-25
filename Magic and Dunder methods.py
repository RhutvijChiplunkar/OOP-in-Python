class Student:

    def __init__(self,name,surname,age):
        self.name=name             #this.name=name
        self.surname=surname
        self.age=age

    #method to return full name
    def FullName(self):
        return "{} {}".format(self.name,self.surname)

    def __repr__(self):
        return "Student('{}','{}',{})".format(self.name,self.surname,self.age)

    def __str__(self):
        return "{} of age {}".format(self.FullName(),self.age)

    def __add__(self, other):
        return self.age+other.age

    def __len__(self):
        return len(self.FullName())

#DUNDER-->double underscore
S1=Student('Sachin','Tendulkar',25)
S2=Student('Virat','Kohli',15)
print("-----------------")
print("for repr and str")
print(S1.FullName())
print(S1.__repr__())
print(S1.__str__())

#dunder add
print("-----------------")
print("for dunder add")
print(S1.__add__(S2))

#dunder len
print("-----------------")
print("for dunder len")
print(S1.__len__())
print(S2.__len__())
print("-----------------")
