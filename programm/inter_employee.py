# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inter_employee.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 478)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(69, 159, 166, 255), stop:1 rgba(255, 255, 255, 194));")
        MainWindow.setIconSize(QSize(40, 40))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(430, 140, 301, 101))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")
        icon = QIcon()
        icon.addFile(u"C:/Users/user/Documents/GitHub/Programm_ing/icons/content_paste_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(40, 40))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(70, 140, 291, 101))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/user/Documents/GitHub/Programm_ing/icons/description_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(40, 40))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(70, 270, 291, 101))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/user/Documents/GitHub/Programm_ing/icons/list_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(40, 40))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(430, 270, 301, 101))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/user/Documents/GitHub/Programm_ing/icons/content_paste_search_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QSize(40, 40))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043e\u0446\u0435\u043d\u043a\u0438", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0440\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0443\u0441\u043f\u0435\u0432\u0430\u0435\u043c\u043e\u0441\u0442\u044c", None))
    # retranslateUi

