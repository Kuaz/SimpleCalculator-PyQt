import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hesap Makinesi')
        self.setGeometry(300, 300, 300, 300)
        
        vbox = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        vbox.addWidget(self.display)
        
        hbox1 = QHBoxLayout()
        btn7 = QPushButton('7')
        btn7.clicked.connect(lambda: self.add_to_display('7'))
        hbox1.addWidget(btn7)
        
        btn8 = QPushButton('8')
        btn8.clicked.connect(lambda: self.add_to_display('8'))
        hbox1.addWidget(btn8)
        
        btn9 = QPushButton('9')
        btn9.clicked.connect(lambda: self.add_to_display('9'))
        hbox1.addWidget(btn9)
        
        btn_divide = QPushButton('/')
        btn_divide.clicked.connect(lambda: self.add_to_display('/'))
        hbox1.addWidget(btn_divide)
        
        vbox.addLayout(hbox1)
        
        hbox2 = QHBoxLayout()
        btn4 = QPushButton('4')
        btn4.clicked.connect(lambda: self.add_to_display('4'))
        hbox2.addWidget(btn4)
        
        btn5 = QPushButton('5')
        btn5.clicked.connect(lambda: self.add_to_display('5'))
        hbox2.addWidget(btn5)
        
        btn6 = QPushButton('6')
        btn6.clicked.connect(lambda: self.add_to_display('6'))
        hbox2.addWidget(btn6)
        
        btn_multiply = QPushButton('*')
        btn_multiply.clicked.connect(lambda: self.add_to_display('*'))
        hbox2.addWidget(btn_multiply)
        
        vbox.addLayout(hbox2)
        
        hbox3 = QHBoxLayout()
        btn1 = QPushButton('1')
        btn1.clicked.connect(lambda: self.add_to_display('1'))
        hbox3.addWidget(btn1)
        
        btn2 = QPushButton('2')
        btn2.clicked.connect(lambda: self.add_to_display('2'))
        hbox3.addWidget(btn2)
        
        btn3 = QPushButton('3')
        btn3.clicked.connect(lambda: self.add_to_display('3'))
        hbox3.addWidget(btn3)
        
        btn_minus = QPushButton('-')
        btn_minus.clicked.connect(lambda: self.add_to_display('-'))
        hbox3.addWidget(btn_minus)
        
        vbox.addLayout(hbox3)
        
        hbox4 = QHBoxLayout()
        btn0 = QPushButton('0')
        btn0.clicked.connect(lambda: self.add_to_display('0'))
        hbox4.addWidget(btn0)
        
        btn_clear = QPushButton('C')
        btn_clear.clicked.connect(lambda: self.display.clear())
        hbox4.addWidget(btn_clear)
        
        btn_equals = QPushButton('=')
        btn_equals.clicked.connect(self.evaluate)
        hbox4.addWidget(btn_equals)
        
        btn_plus = QPushButton('+')
        btn_plus.clicked.connect(lambda: self.add_to_display('+'))
        hbox4.addWidget(btn_plus)
        
        vbox.addLayout(hbox4)
        
        self.setLayout(vbox)
    
    def add_to_display(self, value):
        self.display.setText(self.display.text() + value)
    
    def evaluate(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except:
            self.display.setText('Geçersiz İşlem')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

