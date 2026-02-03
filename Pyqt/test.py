import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
# ui_test.py에서 Ui MainWindow를 import한다.
from ui_test_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        # setupUi 함수를 호출해 MainWindow에 있는 위젯을 배치한다.
        self.ui.setupUi(self)

        # button clicked 이벤트 핸들러로 button_clicked 함수와 연결한다.
        self.ui.pushButton.clicked.connect(self.button_clicked)
        # button clicked 이벤트 핸들러로 button_clicked 함수와 연결한다.
        self.ui.btn_1.clicked.connect(self.button1Function)
        self.ui.btn_2.clicked.connect(self.button2Function)
        self.ui.id_line.textChanged.connect(self.id_text_changed)
        self.ui.pw_line.textChanged.connect(self.pw_text_changed)

    def id_text_changed(self):
        self.ui.btn_1.setText(self.ui.id_line.text())
    def pw_text_changed(self):
        self.ui.btn_2.setText(self.ui.pw_line.text())
    #btn_1이 눌리면 작동할 함수
    def button1Function(self) :
        self.ui.line_1.setText("btn_1 Clicked")

    #btn_2가 눌리면 작동할 함수
    def button2Function(self) :
        self.ui.line_1.setText("btn_2 Clicked")

    def button_clicked(self):
    	# input 위젯의 텍스트를 output 위젯에 셋한다.
        inputText = self.ui.lineEdit.text()
        self.ui.lineEdit_2.setText('{0}'.format(inputText))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
