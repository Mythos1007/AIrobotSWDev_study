# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(603, 525)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(60, 60, 481, 461))
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.name_line = QLineEdit(self.stackedWidgetPage1)
        self.name_line.setObjectName(u"name_line")
        self.name_line.setGeometry(QRect(130, 160, 211, 61))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        self.name_line.setFont(font)
        self.name_label = QLabel(self.stackedWidgetPage1)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(70, 150, 71, 81))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        self.name_label.setFont(font1)
        self.btn_login = QPushButton(self.stackedWidgetPage1)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(350, 160, 61, 61))
        self.btn_login.setFont(font)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.input_line = QLineEdit(self.stackedWidgetPage2)
        self.input_line.setObjectName(u"input_line")
        self.input_line.setGeometry(QRect(60, 310, 291, 41))
        self.btn_send = QPushButton(self.stackedWidgetPage2)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setGeometry(QRect(360, 310, 61, 41))
        self.output_list = QListWidget(self.stackedWidgetPage2)
        self.output_list.setObjectName(u"output_list")
        self.output_list.setGeometry(QRect(60, 20, 361, 271))
        self.btn_exit = QPushButton(self.stackedWidgetPage2)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(10, 20, 41, 41))
        self.stackedWidget.addWidget(self.stackedWidgetPage2)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"Login", None))
        self.btn_send.setText(QCoreApplication.translate("Form", u"Send", None))
        self.btn_exit.setText(QCoreApplication.translate("Form", u"EXIT", None))
    # retranslateUi

