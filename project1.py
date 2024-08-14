#polymorphism in py
class person():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def sum(self,a,b):
        return a+b
    
class student(person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade=grade
    def sum(self,a,b):

        return a*b
    
s1=student("ali",23,"A+")
print(super(student,s1).sum(10,12))