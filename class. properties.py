# class MyClass:
#     x = 5
    
# p1 = MyClass()
# print(p1.x)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = Person("John",36)

# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1 = Person("Jogn",36)
# print(p1)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f" {self.name}( {self.age})"
# p1 = Person('John',36)
# print(p1)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def myfunc(self):
#         print("Hello my name is "+self.name)
        
# p1 = Person('John', 36)
# p1.myfunc()

class Employee:
    def __init__(self,name):
        self.name = name
        
class Dancer:
    def __init__(self,dance):
        self.dance = dance
      
class EmployeeDancer (Employee,Dancer):  
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name
       
o = EmployeeDancer('Kathak','shivani')
print(o.name)
print(o.dance)
