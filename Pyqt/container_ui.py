# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'container.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(568, 476)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(40, 20, 491, 421))
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.btn_next1page = QPushButton(self.stackedWidgetPage1)
        self.btn_next1page.setObjectName(u"btn_next1page")
        self.btn_next1page.setGeometry(QRect(30, 120, 95, 25))
        self.label = QLabel(self.stackedWidgetPage1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 121, 81))
        self.btn_previous1page = QPushButton(self.stackedWidgetPage1)
        self.btn_previous1page.setObjectName(u"btn_previous1page")
        self.btn_previous1page.setGeometry(QRect(30, 160, 95, 25))
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.btn_next2page = QPushButton(self.stackedWidgetPage2)
        self.btn_next2page.setObjectName(u"btn_next2page")
        self.btn_next2page.setGeometry(QRect(30, 120, 95, 25))
        self.label_4 = QLabel(self.stackedWidgetPage2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 20, 121, 81))
        self.btn_previous2page = QPushButton(self.stackedWidgetPage2)
        self.btn_previous2page.setObjectName(u"btn_previous2page")
        self.btn_previous2page.setGeometry(QRect(30, 160, 95, 25))
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QWidget()
        self.stackedWidgetPage3.setObjectName(u"stackedWidgetPage3")
        self.label_5 = QLabel(self.stackedWidgetPage3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 121, 81))
        self.btn_next3page = QPushButton(self.stackedWidgetPage3)
        self.btn_next3page.setObjectName(u"btn_next3page")
        self.btn_next3page.setGeometry(QRect(30, 120, 95, 25))
        self.btn_previous3page = QPushButton(self.stackedWidgetPage3)
        self.btn_previous3page.setObjectName(u"btn_previous3page")
        self.btn_previous3page.setGeometry(QRect(30, 160, 95, 25))
        self.stackedWidget.addWidget(self.stackedWidgetPage3)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_next1page.setText(QCoreApplication.translate("Form", u"NextPage", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tab 1", None))
        self.btn_previous1page.setText(QCoreApplication.translate("Form", u"PreviousPage", None))
        self.btn_next2page.setText(QCoreApplication.translate("Form", u"NextPage", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Tab 2", None))
        self.btn_previous2page.setText(QCoreApplication.translate("Form", u"PreviousPage", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Tab 3", None))
        self.btn_next3page.setText(QCoreApplication.translate("Form", u"NextPage", None))
        self.btn_previous3page.setText(QCoreApplication.translate("Form", u"PreviousPage", None))
    # retranslateUi

