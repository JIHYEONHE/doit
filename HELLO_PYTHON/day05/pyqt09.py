import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random
#홀짝 게임!!!!!!
form_class = uic.loadUiType("pyqt09.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        #self.le_mine.returnPressed.connect(self.myclick) #엔터키 누르면 돌아가게 해주는것!       
 
    def drawStar(self,cnt):
        ret =""
        for i in range(cnt):
            ret +="*"
            
        ret +="\n"
        return ret
    
    def myclick(self):
        a = self.le_first.text()
        b =self.le_last.text()
        aa = int(a)
        bb = int(b)

        txt =""
        for i in range(aa,bb+1):
            txt +=self.drawStar(i)
        
        
        self.te.setText(txt)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()