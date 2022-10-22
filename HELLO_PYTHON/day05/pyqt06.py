import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random
#홀짝 게임!!!!!!
form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.leMine.returnPressed.connect(self.myclick) #엔터키 누르면 돌아가게 해주는것!       
    

    def myclick(self):
        mine = self.leMine.text()
        com =""
        result =""
        
        rnd = random() #랜덤 1까지의 임의의 소수
        if rnd > 0.5:
            com ="홀"
        else:
            com="짝"
            
        if mine == com:
            result = "승리"
        else:
            result = "패배"
            
        self.leCom.setText(com)
        self.leResult.setText(result)
        
       
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()