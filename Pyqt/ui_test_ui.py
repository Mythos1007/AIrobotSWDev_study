# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_test.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 210, 211, 41))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(240, 160, 211, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 170, 67, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 280, 67, 17))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(240, 260, 211, 61))
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(590, 170, 67, 17))
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(510, 200, 95, 51))
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(610, 200, 95, 51))
        self.line_1 = QLineEdit(self.centralwidget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(500, 260, 211, 41))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 60, 67, 17))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 90, 67, 17))
        self.id_line = QLineEdit(self.centralwidget)
        self.id_line.setObjectName(u"id_line")
        self.id_line.setGeometry(QRect(550, 60, 113, 25))
        self.pw_line = QLineEdit(self.centralwidget)
        self.pw_line.setObjectName(u"pw_line")
        self.pw_line.setGeometry(QRect(550, 90, 113, 25))
        self.pw_line.setEchoMode(QLineEdit.EchoMode.Password)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Click!", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"Btn_1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"Btn_2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
    # retranslateUi

