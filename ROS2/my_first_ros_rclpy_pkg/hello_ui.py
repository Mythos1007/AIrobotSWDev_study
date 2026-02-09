# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hello.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_pub_cancel = QPushButton(self.centralwidget)
        self.btn_pub_cancel.setObjectName(u"btn_pub_cancel")
        self.btn_pub_cancel.setGeometry(QRect(280, 70, 95, 31))
        self.btn_subscriber = QPushButton(self.centralwidget)
        self.btn_subscriber.setObjectName(u"btn_subscriber")
        self.btn_subscriber.setGeometry(QRect(160, 110, 95, 31))
        self.label_sub = QLabel(self.centralwidget)
        self.label_sub.setObjectName(u"label_sub")
        self.label_sub.setGeometry(QRect(70, 120, 67, 17))
        self.label_pub = QLabel(self.centralwidget)
        self.label_pub.setObjectName(u"label_pub")
        self.label_pub.setGeometry(QRect(70, 80, 67, 17))
        self.btn_sub_cancel = QPushButton(self.centralwidget)
        self.btn_sub_cancel.setObjectName(u"btn_sub_cancel")
        self.btn_sub_cancel.setGeometry(QRect(280, 110, 95, 31))
        self.btn_publisher = QPushButton(self.centralwidget)
        self.btn_publisher.setObjectName(u"btn_publisher")
        self.btn_publisher.setGeometry(QRect(160, 70, 95, 31))
        self.msg_list = QListWidget(self.centralwidget)
        self.msg_list.setObjectName(u"msg_list")
        self.msg_list.setGeometry(QRect(400, 50, 351, 461))
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
        self.btn_pub_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_subscriber.setText(QCoreApplication.translate("MainWindow", u"Subscribe", None))
        self.label_sub.setText(QCoreApplication.translate("MainWindow", u"Subscribe", None))
        self.label_pub.setText(QCoreApplication.translate("MainWindow", u"Publisher", None))
        self.btn_sub_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_publisher.setText(QCoreApplication.translate("MainWindow", u"Publish", None))
    # retranslateUi

