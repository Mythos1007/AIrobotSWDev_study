from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.btn_showDialog = QPushButton(Form)
        self.btn_showDialog.setObjectName(u"btn_showDialog")
        self.btn_showDialog.setGeometry(QRect(30, 10, 161, 41))
        self.btn_showCritical = QPushButton(Form)
        self.btn_showCritical.setObjectName(u"btn_showCritical")
        self.btn_showCritical.setGeometry(QRect(30, 70, 161, 41))
        self.btn_showWarning = QPushButton(Form)
        self.btn_showWarning.setObjectName(u"btn_showWarning")
        self.btn_showWarning.setGeometry(QRect(30, 130, 161, 41))
        self.btn_showQuestion = QPushButton(Form)
        self.btn_showQuestion.setObjectName(u"btn_showQuestion")
        self.btn_showQuestion.setGeometry(QRect(30, 190, 161, 41))
        self.btn_inputDialog = QPushButton(Form)
        self.btn_inputDialog.setObjectName(u"btn_inputDialog")
        self.btn_inputDialog.setGeometry(QRect(210, 10, 161, 41))
        self.lbl_result = QLineEdit(Form)
        self.lbl_result.setObjectName(u"lbl_result")
        self.lbl_result.setGeometry(QRect(70, 250, 261, 41))
        self.btn_multiLineDialog = QPushButton(Form)
        self.btn_multiLineDialog.setObjectName(u"btn_multiLineDialog")
        self.btn_multiLineDialog.setGeometry(QRect(210, 70, 161, 41))
        self.btn_getIntDialog = QPushButton(Form)
        self.btn_getIntDialog.setObjectName(u"btn_getIntDialog")
        self.btn_getIntDialog.setGeometry(QRect(210, 130, 161, 41))
        self.btn_getItemDialog = QPushButton(Form)
        self.btn_getItemDialog.setObjectName(u"btn_getItemDialog")
        self.btn_getItemDialog.setGeometry(QRect(210, 190, 161, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_showDialog.setText(QCoreApplication.translate("Form", u"MessageBox_inform", None))
        self.btn_showCritical.setText(QCoreApplication.translate("Form", u"MessageBox_critical", None))
        self.btn_showWarning.setText(QCoreApplication.translate("Form", u"MessageBox_warning", None))
        self.btn_showQuestion.setText(QCoreApplication.translate("Form", u"MessageBox_question", None))
        self.btn_inputDialog.setText(QCoreApplication.translate("Form", u"InputDialog", None))
        self.btn_multiLineDialog.setText(QCoreApplication.translate("Form", u"multiLineDialog", None))
        self.btn_getIntDialog.setText(QCoreApplication.translate("Form", u"getIntDialog", None))
        self.btn_getItemDialog.setText(QCoreApplication.translate("Form", u"getitemDialog", None))
    # retranslateUi

