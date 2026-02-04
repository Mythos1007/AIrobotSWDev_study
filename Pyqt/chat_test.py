import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
# ui_test.py에서 Ui MainWindow를 import한다.
from chat_ui import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        # setupUi 함수를 호출해 MainWindow에 있는 위젯을 배치한다.
        self.ui.setupUi(self)

        self.ui.btn_login.clicked.connect(self.btn_login_clicked)
        self.ui.btn_exit.clicked.connect(self.btn_exit_clicked)
        self.ui.btn_send.clicked.connect(self.btn_send_clicked)
        self.ui.stackedWidget.setCurrentIndex(0)

    def btn_login_clicked(self):
        if self.ui.name_line.text().strip() == '':
            pass
        else:
            self.ui.stackedWidget.setCurrentIndex(1)

    def btn_send_clicked(self):
        name = self.ui.name_line.text()
        input_text = self.ui.input_line.text()
        self.ui.output_list.addItem(f'{name}: {input_text}')
        self.ui.input_line.clear()

    def btn_exit_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
