import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QFile
# ui_test.py에서 Ui FORM을 import한다.
from container_ui import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        # setupUi 함수를 호출해 MainWindow에 있는 위젯을 배치한다.
        self.ui.setupUi(self)

        #setCuttentIndex(페이지번호)함수로 현재 페이지를 설정할 수 있습니다.
        self.ui.btn_next1page.clicked.connect(self.next_page_clicked  )
        self.ui.btn_next2page.clicked.connect(self.next_page_clicked)
        self.ui.btn_next3page.clicked.connect(self.next_page_clicked)

        self.ui.btn_previous1page.clicked.connect(self.previous_page_clicked)
        self.ui.btn_previous2page.clicked.connect(self.previous_page_clicked)
        self.ui.btn_previous3page.clicked.connect(self.previous_page_clicked)

    def next_page_clicked(self):
        current_index = self.ui.stackedWidget.currentIndex()
        total_page = self.ui.stackedWidget.count()
        if current_index < total_page -1:
            self.ui.stackedWidget.setCurrentIndex(current_index +1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)

    def previous_page_clicked(self):
        current_index = self.ui.stackedWidget.currentIndex()
        if current_index > 0:
            self.ui.stackedWidget.setCurrentIndex(current_index - 1)
        else:
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.count() - 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
