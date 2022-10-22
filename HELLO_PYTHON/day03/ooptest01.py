class Animal:
    
    def __init__(self):  #initialize 의 줄임말 (초기화) 생성자!!!
        self.hungry = 5
    
    def timegoby(self):
        if self.hungry>0:
            self.hungry -=1
        
    def manttang(self):
        self.hungry=10
        
class Human(Animal):
    
    def __init__(self):
        super().__init__()  #조상 호출(상속 받기위해 super사용)
        self.skill_lang = 0

    def momstouch(self, stroke):
        self.skill_lang += stroke

hum = Human()
print(hum.skill_lang) #0
print(hum.hungry)   #5
hum.manttang() #10
hum.momstouch(11) #0+11
print(hum.hungry) #10
print(hum.skill_lang) #11




    