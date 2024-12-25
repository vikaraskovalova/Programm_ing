

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(837, 715)
        Dialog.setStyleSheet(u"background-color: rgb(69, 159, 166);")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 30, 681, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_6)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(140, 80, 681, 471))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_r_1 = QLabel(self.layoutWidget1)
        self.label_r_1.setObjectName(u"label_r_1")
        self.label_r_1.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.label_r_1)

        self.label_r_2 = QLabel(self.layoutWidget1)
        self.label_r_2.setObjectName(u"label_r_2")
        self.label_r_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.label_r_2)

        self.label_r_3 = QLabel(self.layoutWidget1)
        self.label_r_3.setObjectName(u"label_r_3")
        self.label_r_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.label_r_3)

        self.label_r_4 = QLabel(self.layoutWidget1)
        self.label_r_4.setObjectName(u"label_r_4")
        self.label_r_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.label_r_4)

        self.label_r_5 = QLabel(self.layoutWidget1)
        self.label_r_5.setObjectName(u"label_r_5")
        self.label_r_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.label_r_5)

        self.label_r_6 = QLabel(self.layoutWidget1)
        self.label_r_6.setObjectName(u"label_r_6")
        self.label_r_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.label_r_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_r_7 = QLabel(self.layoutWidget1)
        self.label_r_7.setObjectName(u"label_r_7")
        self.label_r_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.label_r_7)

        self.label_r_8 = QLabel(self.layoutWidget1)
        self.label_r_8.setObjectName(u"label_r_8")
        self.label_r_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.label_r_8)

        self.label_r_9 = QLabel(self.layoutWidget1)
        self.label_r_9.setObjectName(u"label_r_9")
        self.label_r_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.label_r_9)

        self.label_r_10 = QLabel(self.layoutWidget1)
        self.label_r_10.setObjectName(u"label_r_10")
        self.label_r_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.label_r_10)

        self.label_r_11 = QLabel(self.layoutWidget1)
        self.label_r_11.setObjectName(u"label_r_11")
        self.label_r_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.label_r_11)

        self.label_r_12 = QLabel(self.layoutWidget1)
        self.label_r_12.setObjectName(u"label_r_12")
        self.label_r_12.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.label_r_12)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_r_13 = QLabel(self.layoutWidget1)
        self.label_r_13.setObjectName(u"label_r_13")
        self.label_r_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.label_r_13)

        self.label_r_14 = QLabel(self.layoutWidget1)
        self.label_r_14.setObjectName(u"label_r_14")
        self.label_r_14.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.label_r_14)

        self.label_r_15 = QLabel(self.layoutWidget1)
        self.label_r_15.setObjectName(u"label_r_15")
        self.label_r_15.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.label_r_15)

        self.label_r_16 = QLabel(self.layoutWidget1)
        self.label_r_16.setObjectName(u"label_r_16")
        self.label_r_16.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.label_r_16)

        self.label_r_17 = QLabel(self.layoutWidget1)
        self.label_r_17.setObjectName(u"label_r_17")
        self.label_r_17.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.label_r_17)

        self.label_r_18 = QLabel(self.layoutWidget1)
        self.label_r_18.setObjectName(u"label_r_18")
        self.label_r_18.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.label_r_18)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_r_19 = QLabel(self.layoutWidget1)
        self.label_r_19.setObjectName(u"label_r_19")
        self.label_r_19.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.label_r_19)

        self.label_r_20 = QLabel(self.layoutWidget1)
        self.label_r_20.setObjectName(u"label_r_20")
        self.label_r_20.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.label_r_20)

        self.label_r_21 = QLabel(self.layoutWidget1)
        self.label_r_21.setObjectName(u"label_r_21")
        self.label_r_21.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.label_r_21)

        self.label_r_22 = QLabel(self.layoutWidget1)
        self.label_r_22.setObjectName(u"label_r_22")
        self.label_r_22.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.label_r_22)

        self.label_r_23 = QLabel(self.layoutWidget1)
        self.label_r_23.setObjectName(u"label_r_23")
        self.label_r_23.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.label_r_23)

        self.label_r_24 = QLabel(self.layoutWidget1)
        self.label_r_24.setObjectName(u"label_r_24")
        self.label_r_24.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.label_r_24)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_r_25 = QLabel(self.layoutWidget1)
        self.label_r_25.setObjectName(u"label_r_25")
        self.label_r_25.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.label_r_25)

        self.label_r_26 = QLabel(self.layoutWidget1)
        self.label_r_26.setObjectName(u"label_r_26")
        self.label_r_26.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.label_r_26)

        self.label_r_27 = QLabel(self.layoutWidget1)
        self.label_r_27.setObjectName(u"label_r_27")
        self.label_r_27.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.label_r_27)

        self.label_r_28 = QLabel(self.layoutWidget1)
        self.label_r_28.setObjectName(u"label_r_28")
        self.label_r_28.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.label_r_28)

        self.label_r_29 = QLabel(self.layoutWidget1)
        self.label_r_29.setObjectName(u"label_r_29")
        self.label_r_29.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.label_r_29)

        self.label_r_30 = QLabel(self.layoutWidget1)
        self.label_r_30.setObjectName(u"label_r_30")
        self.label_r_30.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.label_r_30)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.layoutWidget2 = QWidget(Dialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 80, 95, 471))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_10)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(240, 590, 381, 121))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u0440\u0435\u0434\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0433", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041f\u044f\u0442\u043d\u0438\u0446\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u0431\u0431\u043e\u0442\u0430", None))
        self.label_r_1.setText("")
        self.label_r_2.setText("")
        self.label_r_3.setText("")
        self.label_r_4.setText("")
        self.label_r_5.setText("")
        self.label_r_6.setText("")
        self.label_r_7.setText("")
        self.label_r_8.setText("")
        self.label_r_9.setText("")
        self.label_r_10.setText("")
        self.label_r_11.setText("")
        self.label_r_12.setText("")
        self.label_r_13.setText("")
        self.label_r_14.setText("")
        self.label_r_15.setText("")
        self.label_r_16.setText("")
        self.label_r_17.setText("")
        self.label_r_18.setText("")
        self.label_r_19.setText("")
        self.label_r_20.setText("")
        self.label_r_21.setText("")
        self.label_r_22.setText("")
        self.label_r_23.setText("")
        self.label_r_24.setText("")
        self.label_r_25.setText("")
        self.label_r_26.setText("")
        self.label_r_27.setText("")
        self.label_r_28.setText("")
        self.label_r_29.setText("")
        self.label_r_30.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"15:00 - 16:30 ", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"8:00 - 9:30", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"9:40 - 11:10", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"11:30 - 13:00", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"13:20 - 14:50", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

