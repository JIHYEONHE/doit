import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt07.ui")[0]
#구구단 구구단 !!!!
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
    
    def myclick(self):
        dan = self.le.text()
        idan = int(dan) #입력 받은 단수를 숫자로 형변환
        txt =""
        
        # txt += str(idan)+"*1"+"="+ str(idan*1)+"\n"
        # txt += str(idan)+"*2"+"="+ str(idan*2)+"\n"
        # txt += str(idan)+"*3"+"="+ str(idan*3)+"\n"
        # txt += str(idan)+"*4"+"="+ str(idan*4)+"\n"
        # txt += str(idan)+"*5"+"="+ str(idan*5)+"\n"
        # txt += str(idan)+"*6"+"="+ str(idan*6)+"\n"
        # txt += str(idan)+"*7"+"="+ str(idan*7)+"\n"
        # txt += str(idan)+"*8"+"="+ str(idan*8)+"\n"
        # txt += str(idan)+"*9"+"="+ str(idan*9)+"\n"
        
        #파이썬 3.5부터 f스트링 사용합니당
        txt += f"{idan}*{1}={idan*1}\n"
        txt += f"{idan}*{2}={idan*2}\n"
        txt += f"{idan}*{3}={idan*3}\n"
        txt += f"{idan}*{4}={idan*4}\n"
        txt += f"{idan}*{5}={idan*5}\n"
        txt += f"{idan}*{6}={idan*6}\n"
        txt += f"{idan}*{7}={idan*7}\n"
        txt += f"{idan}*{8}={idan*8}\n"
        txt += f"{idan}*{9}={idan*9}\n"
        
        
        self.te.setText(txt)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()