import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random
#로또 생성하기
form_class = uic.loadUiType("pyqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
    def myclick(self):
        #arr i in range(1,45)
        # self.lbl.setText("GoodEvening")
        arr45 = [1, 2, 3, 4, 5,             6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15,     16, 17, 18, 19, 20,
        21, 22, 23, 24, 25,     26,27, 28, 29, 30,
        31, 32, 33, 34, 35,     36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45
            ]
        
        for i in range(100):
            rnd = int(random() * len(arr45))
            a = arr45[0]
            b = arr45[rnd]
            arr45[0] = b
            arr45[rnd] = a
    
            lotto = arr45[0:6]
            
        a1 = str(lotto[0])
        a2 = str(lotto[1])
        a3 = str(lotto[2])
        a4 = str(lotto[3])
        a5 = str(lotto[4])
        a6 = str(lotto[5])
        
            
        self.le1.setText(a1)
        self.le2.setText(a2)
        self.le3.setText(a3)
        self.le4.setText(a4)
        self.le5.setText(a5)
        self.le6.setText(a6)
        
    #self.le1.setText(str(arr[0]))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
