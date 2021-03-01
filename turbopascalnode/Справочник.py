from PyQt5.QtWidgets import QMainWindow, QWidget, QMenuBar, QTextBrowser, QPushButton, QApplication
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1024, 768)
        MainWindow.setWindowTitle('Справочник')
        MainWindow.setWindowIcon(QIcon('img.png'))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("border-image:url(prog.jpg);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.page1()

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        tools = self.menubar.addMenu('Поиск по списку')
        tools.addAction("Операторы Turbo Pascal", self.page1)
        tools.addSeparator()
        tools.addAction("1.Присваивание переменной значение выражения", self.page2)
        tools.addSeparator()
        tools.addAction("2.Begin___End", self.page3)
        tools.addSeparator()
        tools.addAction("3.Case___Of___Else___End", self.page4)
        tools.addSeparator()
        tools.addAction("4.For___To, Downto___Do", self.page5)
        tools.addSeparator()
        tools.addAction("5.Goto", self.page6)
        tools.addSeparator()
        tools.addAction("6.If___Then___Else", self.page7)
        tools.addSeparator()
        tools.addAction("7.Вызов процедуры", self.page8)
        tools.addSeparator()
        tools.addAction("8.Repeat___Until", self.page9)
        tools.addSeparator()
        tools.addAction("9.While___Do", self.page10)
        tools.addSeparator()
        tools.addAction("10.With___Do", self.page11)
        tools.addSeparator()
        tools.addAction("11.Inline", self.page12)
        tools.addSeparator()
        tools.addAction("12.Бинарные арифметические операторы", self.page13)
        tools.addSeparator()
        tools.addAction("13.Унарные арифметические операторы", self.page14)
        tools.addSeparator()
        tools.addAction("14.Булевы операторы", self.page15)
        tools.addSeparator()
        tools.addAction("15.Логические операторы", self.page16)
        tools.addSeparator()
        tools.addAction("16.PChar операторы", self.page17)
        tools.addSeparator()
        tools.addAction("17.Операторы сравнения", self.page18)
        tools.addSeparator()
        tools.addAction("18.Операторы множеств", self.page19)
        tools.addSeparator()
        tools.addAction("19.Строковые операторы", self.page20)
        tools.addSeparator()
        tools.addAction("20.Оператор '@'", self.page21)
        tools.triggered.connect(self.list.deleteLater)
        tools.triggered.connect(self.nextButton.deleteLater)
        tools.triggered.connect(self.backButton.deleteLater)

        self.menubar.setStyleSheet("""
                                      background-color: rgb(255, 215, 0);
                                      font: bold;
                                      font-family: Times New Roman;
                                      color: rgb(0, 0, 255);
                                      font-size: 19px;
                                      selection-background-color: white;    
                                      """)
        self.menubar.setGeometry(0, 0, 1024, 30)

    def pageparent(self):

        self.list = QTextBrowser(MainWindow)
        self.list.setStyleSheet("""
                                                      font: bold;
                                                      font-family: Times New Roman;
                                                      color: rgb(0, 0, 255);
                                                      background: rgb(255, 215, 0);
                                                      font-size: 20px;                                                                                                                                                                     
                            """)
        self.list.setGeometry(100, 70, 850, 500)
        self.list.show()

        self.nextButton = QPushButton(MainWindow)
        self.nextButton.setGeometry(QRect(600, 600, 221, 61))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setText("Вперед")
        self.nextButton.setStyleSheet("""
                                                  font: bold;
                                                  font-family: Times New Roman;
                                                  color: rgb(0, 0, 255);
                                                  background: rgb(255, 215, 0);
                                                  font-size: 27px;                                                                                                                                                                     
                        """)

        self.nextButton.show()

        self.backButton = QPushButton(MainWindow)
        self.backButton.setGeometry(QRect(200, 600, 221, 61))
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Назад")
        self.backButton.setStyleSheet("""
                                                         font: bold;
                                                         font-family: Times New Roman;
                                                         color: rgb(0, 0, 255);
                                                         background: rgb(255, 215, 0);
                                                         font-size: 27px;""")
        self.backButton.show()

        self.nextButton.clicked.connect(self.list.deleteLater)
        self.nextButton.clicked.connect(self.nextButton.deleteLater)
        self.nextButton.clicked.connect(self.backButton.deleteLater)
        self.backButton.clicked.connect(self.list.deleteLater)
        self.backButton.clicked.connect(self.nextButton.deleteLater)
        self.backButton.clicked.connect(self.backButton.deleteLater)

    def page1(self):

        self.pageparent()

        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[1:17]:
              text += line + '\n'
        self.list.setPlainText(text)

        self.nextButton.clicked.connect(self.page2)
        self.backButton.clicked.connect(self.page21)

    def page2(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[18:27]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page3)
        self.backButton.clicked.connect(self.page1)

    def page3(self):
        
        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[28:47]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page4)
        self.backButton.clicked.connect(self.page2)

    def page4(self):
        
        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[48:74]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page5)
        self.backButton.clicked.connect(self.page3)

    def page5(self):
        
        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[75:98]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page6)
        self.backButton.clicked.connect(self.page4)

    def page6(self):
        
        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[99:114]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page7)
        self.backButton.clicked.connect(self.page5)

    def page7(self):
        
        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[115:138]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page8)
        self.backButton.clicked.connect(self.page6)

    def page8(self):
       
        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[139:164]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page9)
        self.backButton.clicked.connect(self.page7)

    def page9(self):
       
        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[165:186]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page10)
        self.backButton.clicked.connect(self.page8)

    def page10(self):
        
        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[187:204]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page11)
        self.backButton.clicked.connect(self.page9)

    def page11(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[205:224]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page12)
        self.backButton.clicked.connect(self.page10)

    def page12(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[225:249]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page13)
        self.backButton.clicked.connect(self.page11)

    def page13(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[250:262]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page14)
        self.backButton.clicked.connect(self.page12)

    def page14(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[263:276]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page15)
        self.backButton.clicked.connect(self.page13)

    def page15(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[277:287]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page16)
        self.backButton.clicked.connect(self.page14)

    def page16(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[288:301]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page17)
        self.backButton.clicked.connect(self.page15)

    def page17(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[302:314]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page18)
        self.backButton.clicked.connect(self.page16)

    def page18(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[315:334]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page19)
        self.backButton.clicked.connect(self.page17)

    def page19(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[335:347]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page20)
        self.backButton.clicked.connect(self.page18)

    def page20(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[348:354]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page21)
        self.backButton.clicked.connect(self.page19)

    def page21(self):

        self.pageparent()
        with open('text.txt') as file:
            lines = file.readlines()
            text = ""
            for line in lines[355:365]:
                text += line + '\n'
        self.list.setPlainText(text)
        self.nextButton.clicked.connect(self.page1)
        self.backButton.clicked.connect(self.page20)

if __name__ == "__main__":


    import sys

    app = QApplication(sys.argv)
    app.setStyle('Windows')
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())































