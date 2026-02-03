# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)
import myqrc.youtube_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ytb_img = QLabel(self.centralwidget)
        self.ytb_img.setObjectName(u"ytb_img")
        self.ytb_img.setGeometry(QRect(320, 90, 401, 291))
        self.ytb_img.setPixmap(QPixmap(u":/newPrefix/image-Photoroom.png"))
        self.id_line = QLineEdit(self.centralwidget)
        self.id_line.setObjectName(u"id_line")
        self.id_line.setGeometry(QRect(180, 240, 141, 21))
        self.pw_line = QLineEdit(self.centralwidget)
        self.pw_line.setObjectName(u"pw_line")
        self.pw_line.setGeometry(QRect(180, 280, 141, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 240, 67, 17))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 280, 67, 17))
        self.login_b = QPushButton(self.centralwidget)
        self.login_b.setObjectName(u"login_b")
        self.login_b.setGeometry(QRect(340, 240, 95, 61))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(520, 320, 81, 91))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 60, 111, 22))
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 10, 111, 22))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(620, 320, 101, 161))
        self.radioButton_6 = QRadioButton(self.groupBox_2)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(10, 130, 111, 22))
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(10, 10, 111, 22))
        self.radioButton_5 = QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(10, 90, 111, 22))
        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(10, 50, 111, 22))
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(100, 320, 121, 61))
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(220, 320, 121, 61))
        self.comboBox_1 = QComboBox(self.centralwidget)
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setGeometry(QRect(500, 140, 86, 25))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(630, 140, 86, 25))
        self.checkBox_1 = QCheckBox(self.centralwidget)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setGeometry(QRect(350, 320, 91, 22))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(350, 360, 91, 22))
        self.line_1 = QLineEdit(self.centralwidget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(100, 390, 331, 31))
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
        self.ytb_img.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_b.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.groupBox.setTitle("")
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.groupBox_2.setTitle("")
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Like", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Premium", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Sub", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Music", None))
        self.btn_1.setText("")
        self.btn_2.setText("")
        self.checkBox_1.setText(QCoreApplication.translate("MainWindow", u"remember", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"auto", None))
    # retranslateUi

