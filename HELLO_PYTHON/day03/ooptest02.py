class Car:
    def __init__(self): #생성자
        self.speed = 0
        print("생성",self.speed)
    
    def accel(self,strength):
        self.speed += strength
        
    def __del__(self):   #소멸자 #자바에는 garbage collector가 있음
        self.speed = 0 
        print("제거 소멸",self.speed)
        
        
if __name__ == '__main__':    
    c = Car()
    print(c.speed) #0
    c.accel(100) #100
    print(c.speed) #100

        