from astropy.units import mg
from Cython.Compiler.Naming import self_cname
class Byden:
    def __init__(self):
        self.ac = 10
    def makewar(self):
        self.ac -= 1
    
class Putin:
    def __init__(self):
        self.nuclear = 6660
    def altzheimer(self):
        self.nuclear -= 1
        
class Mugun(Byden,Putin): #다중상속!!
    def __init__(self): 
        Byden.__init__(self)  #다중상속 할때는 super가 아닌 따로 init(self)해줘야함
        Putin.__init__(self)
       

mg = Mugun()
print(mg.ac)#10
print(mg.nuclear)#6660
mg.makewar()#9
mg.altzheimer()#6659
print(mg.ac)#9
print(mg.nuclear)#6659

    