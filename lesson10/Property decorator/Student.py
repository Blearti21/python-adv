from Main import student1


class Student:

    def __init__(self , name, age):
         self.name = name
         self.age = age



    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def name(self,name):
        self.__name=name

    @property
    def age(self,age):
        self.__age=age


studenti = Student("Edeni", 17)

print(studenti.age)
print(studenti.name)

studenti.name = "Driarti"
studenti.age = "15"

print(studenti.age)
print(studenti.name)


