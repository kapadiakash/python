# class Car:
#     def __init__(self,make,model,year,color,fuel_type,is_running,speed):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.color=color
#         self.fuel_type=fuel_type
#         self.is_running=is_running
#         self.speed=speed
    
#     def __init__

class Parent:
    def __init__(self):
        print('parent class constructor')
        
    def parent_property(self):
        print('parent''s property')

class Child(Parent):
    def __init__(self):
        print('child class constructor')
        
    def child_property(self):
        print('child''s property')
        
# ch = Child()
# ch.child_property()
# ch.parent_property()

# a = Parent()
# a.parent_property()
# a.child_property()     #no use parent to child property

# class Parent:
#     def __init__(self):
#         print('parent class constructor')
    
#     def parent_property(self):
#         print('parent''s property')
        
# class Child(Parent):
#     def __init__(self):
#         print('child class constructor')
        
#     def child_property(self):
#         print('child''s property')
        
# ch = Child()
# ch.child_property()
# ch.parent_property()

# p=Parent()
# p.parent_property()

#                                   Single inheritance
# class KKK:
#     def __init__(self):
#         print('akash')
        
#     def K(self):
#         print('Hii')
        
# class LLL(KKK):
#     def __init__(self):
#         print('my name is ')
    
#     def L (self):
#         print('Hello')

# a = LLL()

# a.K()

# a.L()

# LLL()


# KKK()

                              
# class AaA:
#     def __init__(self):
#         print('kalamkhande')
        
#     def AaA (self):
#         print('villege')
        
# class BbB (AaA):
#     def __init__(self):
#         print("my")
        
#     def BbB (self):
#         print('name is')
        
# BbB()

# b = BbB()
# b.AaA()

# b.BbB()

# AaA()
#                           multi_level-inheritance

# class AaA:
#     def __init__(self):
#         print("hello sir good morning")
        
#     def AaA (self):
#         print('My hobby is sing a song and computer operating')
        
# class BbB(AaA):
#     def __init__(self):
#         super().__init__()
#         print('my name is akash kapadi')
    
#     def BbB(self):
#         print('as well as i also done small cource which is python devoloper')


# class CcC(BbB):
#     def __init__(self):
#         super().__init__()
#         print('First of all thanku so much for to give me this opportunity')
        
#     def CcC(self):
#         print("i am a graduate form JSM college shivale")


# c = CcC()
# c.CcC()
# c.BbB()
# c.AaA()

class Parent:                                # Parent class or Base Class or Super Class
    def __init__(self):
        print("parent class Constructor")

    def parent_property(self):
        print('parent''s property')

class Child(Parent):                          # Child class or Derived class or Sub Class
    def __init__(self):
        super().__init__()
        print('Child class Constructor')
    
    def child_property(self):
        print('Child''s property')

class GrandChild(Child):                         
    def __init__(self):
        super().__init__()
        print('GrandChild class Constructor')
    
    def grandchild_property(self):
        print('GrandChild''s property')

# Creating an instance of the GrandChild class (Child Class)
gc = GrandChild()     
gc.grandchild_property()
gc.child_property()
gc.parent_property()

# Creating an instance of the Child class (Child Class)
c=Child()
c.child_property()
# c.grandchild_property()

# Creating an instance of the parent class (Parent Class)
parent=Parent()
parent.parent_property()
# parent.child_property()    # Parent class cannot access child class method

print()