class Parent:
    def __init__(self):
        print("parent class Constructor")
        
    def parent_property(self):
        print('parent''s property')
        
class Brother(Parent):
    def __init__(self):
        super().__init__()
        print('child class property')
        
    def brother_property(self):
        print('child''s property')
        
class Sister(Parent):
    def __init__(self):
        super().__init__()
        print('Grandchild class constructor')
        
    def sister_property(self):
        print('grandchild''s property')
        
b = Brother()
b.brother_property()
b.parent_property()