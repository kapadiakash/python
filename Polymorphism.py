class A:
    def alpha(self):
        pass
    
class a(A):
    def alpha(self):
        print('it is a first alphabet')
        
class b (A):
    def alpha(self):
        print('it is second alphabet')
        
class c(A):
    def alpha(self):
        print('it is third alphabet')
        
def perform_alpha(A):
    A.alpha()
    
aa = a()
bb = b()
cc = c()


perform_alpha(aa)
perform_alpha(bb)
perform_alpha(cc)