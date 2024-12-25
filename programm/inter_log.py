# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inter_log.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(738, 626)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(69, 159, 166, 255), stop:1 rgba(255, 255, 255, 194));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 280, 61, 41))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"color: white; ")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 380, 101, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"color: white;")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(290, 320, 191, 51))
        self.textEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  ")
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(290, 410, 191, 51))
        self.textEdit_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  ")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 490, 111, 51))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 320, 61, 51))
        self.label_4.setStyleSheet(u"image: url(C:/Users/user/Documents/GitHub/Programm_ing/icons/passkey_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg);\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 2px solid white; \n"
"border-radius: 10px; \n"
"  ")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 410, 61, 51))
        self.label_5.setStyleSheet(u"image: url(C:/Users/user/Documents/GitHub/Programm_ing/icons/vpn_key_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg);\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 2px solid white; \n"
"border-radius: 10px; ")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(320, 110, 131, 131))
        self.widget.setStyleSheet(u"image: url(C:/Users/user/Documents/GitHub/Programm_ing/icons/person_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg);\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius:60px; \n"
"padding: 5px;  ")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 240, 491, 41))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"color: white; ")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(250, 490, 51, 51))
        self.label_7.setStyleSheet(u"image: url(C:/Users/user/Documents/GitHub/Programm_ing/icons/login_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg);\n"
"background-color: rgba(255, 255, 255, 0); \n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0421 \u0414\u0435\u043a\u0430\u043d\u0430\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0438\u0440\u0443\u0439\u0442\u0435\u0441\u044c, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f \u043a \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u043c", None))
        self.label_7.setText("")
    # retranslateUi

