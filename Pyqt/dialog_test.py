import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit
from PySide6.QtCore import QFile
from dialog_ui import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        # setupUi 함수를 호출해 MainWindow에 있는 위젯을 배치한다.
        self.ui.setupUi(self)
        self.ui.btn_showDialog.clicked.connect(self.btn_showDialog_clicked)
        self.ui.btn_showCritical.clicked.connect(self.btn_showCritical_clicked)
        self.ui.btn_showWarning.clicked.connect(self.btn_showWarning_clicked)
        self.ui.btn_showQuestion.clicked.connect(self.btn_showQuestion_clicked)
        self.ui.btn_inputDialog.clicked.connect(self.btn_inputDialog_clicked)

        self.ui.btn_getItemDialog.clicked.connect(self.btn_getItemDialog_clicked)

    def btn_showDialog_clicked(self):
        result = QMessageBox.information(
                   self,
                   'Message',
                   'This is an information message.',
                   QMessageBox.Ok | QMessageBox.Cancel,
                   QMessageBox.Ok)
        # 사용자가 어떤 버튼을 눌렀는지 출력
        print('Dialog result:', result)

    def btn_showCritical_clicked(self):
        result = QMessageBox.critical(
                     self,
                     'Critical',
                     'This is an critical error message',
                     QMessageBox.Ok, QMessageBox.Ok)
          # 사용자가 어떤 버튼을 눌렀는지 출력
        print('Dialog result:', result)

    def btn_showWarning_clicked(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Warning')
        msg.setText('This is a warning message.')
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec()
        # 사용자가 어떤 버튼을 눌렀는지 출력
        print('Dialog result:', result)

    def btn_showQuestion_clicked(self):
        result = QMessageBox.question(
                   self,
                   'Question Message',
                   'choice Yes or No',
                   QMessageBox.Yes| QMessageBox.No,
                   QMessageBox.Yes)

        # 사용자 응답에 따라 행동
        if result == QMessageBox.Yes:
            print('User chose Yes')
        else:
            print('User chose No')

        # 사용자가 어떤 버튼을 눌렀는지 출력
        print('Dialog result:', result)

    def btn_inputDialog_clicked(self):
        ret_text, is_ok = QInputDialog.getText(
                self,
                "Input Text",
                "Enter Your Text!",
                QLineEdit.PasswordEchoOnEdit,
                "default text!",
                )
        if is_ok:
            self.ui.lbl_result.setText(f'{ret_text}')

    def btn_getItemDialog_clicked(self):
        ret_item, is_ok = QInputDialog.getItem(
                self,
                "Input Item",
                "Enter Your Item!",
                ['one','two','three'],
                0,
                )
        if is_ok:
            self.ui.lbl_result.setText(f'{ret_item}')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
