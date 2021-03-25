class Student:

    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

    # @property is used to access the method as variable
    @property
    def email(self):
        return "{}.{}@python.com".format(self.name,self.surname)

    @property
    def FullName(self):
        return "{} {}".format(self.name,self.surname)

    #Setter method to set the value
    @FullName.setter
    def FullName(self,nm):
        fname,lname=nm.split(" ")
        self.name=fname
        self.surname=lname

    #Deleter method to delete data
    @FullName.deleter
    def FullName(self):
        print("Name deleted")
        self.name=None
        self.surname=None

print("-------------------")
#initially S with given input name will be created
S=Student('Sachin','Tendulkar')

#It will set the value (replace the previous)
S.FullName="Virat Kohli"

#we can access methods like variables
print(S.FullName)
print(S.email)
print("-------------------")

#delete the full name
del S.FullName
print(S.name)       #It will print None
print("-------------------")
