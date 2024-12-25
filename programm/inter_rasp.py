

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(837, 715)
        Dialog.setStyleSheet(u"background-color: rgb(69, 159, 166);")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(140, 540, 121, 41))
        font = QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 540, 81, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);  \n"
"color: white;")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 80, 681, 33))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_6)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(130, 130, 681, 391))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit_1 = QTextEdit(self.widget1)
        self.textEdit_1.setObjectName(u"textEdit_1")
        self.textEdit_1.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.textEdit_1)

        self.textEdit_2 = QTextEdit(self.widget1)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.textEdit_3 = QTextEdit(self.widget1)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.textEdit_3)

        self.textEdit_4 = QTextEdit(self.widget1)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.textEdit_4)

        self.textEdit_5 = QTextEdit(self.widget1)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.textEdit_5)

        self.textEdit_6 = QTextEdit(self.widget1)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.textEdit_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit_7 = QTextEdit(self.widget1)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.textEdit_7)

        self.textEdit_8 = QTextEdit(self.widget1)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.textEdit_8)

        self.textEdit_9 = QTextEdit(self.widget1)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.textEdit_9)

        self.textEdit_10 = QTextEdit(self.widget1)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.textEdit_10)

        self.textEdit_11 = QTextEdit(self.widget1)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.textEdit_11)

        self.textEdit_12 = QTextEdit(self.widget1)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_3.addWidget(self.textEdit_12)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textEdit_13 = QTextEdit(self.widget1)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.textEdit_13)

        self.textEdit_14 = QTextEdit(self.widget1)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.textEdit_14)

        self.textEdit_15 = QTextEdit(self.widget1)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.textEdit_15)

        self.textEdit_16 = QTextEdit(self.widget1)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.textEdit_16)

        self.textEdit_17 = QTextEdit(self.widget1)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.textEdit_17)

        self.textEdit_18 = QTextEdit(self.widget1)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_4.addWidget(self.textEdit_18)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textEdit_19 = QTextEdit(self.widget1)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.textEdit_19)

        self.textEdit_20 = QTextEdit(self.widget1)
        self.textEdit_20.setObjectName(u"textEdit_20")
        self.textEdit_20.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.textEdit_20)

        self.textEdit_21 = QTextEdit(self.widget1)
        self.textEdit_21.setObjectName(u"textEdit_21")
        self.textEdit_21.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.textEdit_21)

        self.textEdit_22 = QTextEdit(self.widget1)
        self.textEdit_22.setObjectName(u"textEdit_22")
        self.textEdit_22.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.textEdit_22)

        self.textEdit_23 = QTextEdit(self.widget1)
        self.textEdit_23.setObjectName(u"textEdit_23")
        self.textEdit_23.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.textEdit_23)

        self.textEdit_24 = QTextEdit(self.widget1)
        self.textEdit_24.setObjectName(u"textEdit_24")
        self.textEdit_24.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.textEdit_24)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textEdit_26 = QTextEdit(self.widget1)
        self.textEdit_26.setObjectName(u"textEdit_26")
        self.textEdit_26.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.textEdit_26)

        self.textEdit_25 = QTextEdit(self.widget1)
        self.textEdit_25.setObjectName(u"textEdit_25")
        self.textEdit_25.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.textEdit_25)

        self.textEdit_27 = QTextEdit(self.widget1)
        self.textEdit_27.setObjectName(u"textEdit_27")
        self.textEdit_27.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.textEdit_27)

        self.textEdit_28 = QTextEdit(self.widget1)
        self.textEdit_28.setObjectName(u"textEdit_28")
        self.textEdit_28.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.textEdit_28)

        self.textEdit_29 = QTextEdit(self.widget1)
        self.textEdit_29.setObjectName(u"textEdit_29")
        self.textEdit_29.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.textEdit_29)

        self.textEdit_30 = QTextEdit(self.widget1)
        self.textEdit_30.setObjectName(u"textEdit_30")
        self.textEdit_30.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.textEdit_30)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.widget2 = QWidget(Dialog)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 130, 95, 391))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_11)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(220, 590, 381, 121))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 4px solid white; \n"
"border-radius: 6px; \n"
"padding: 5px;  \n"
"color: white;")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font2)
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
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u0421\u0410\u0423-22-1\u0431", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u0421\u0410\u0423-23-1\u0431", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u0421\u0410\u0423-24-1\u0431", None))

        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0421\u0440\u0435\u0434\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0433", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041f\u044f\u0442\u043d\u0438\u0446\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0421\u0443\u0431\u0431\u043e\u0442\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"8:00 - 9:30", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"9:40 - 11:10", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"11:30 - 13:00", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"13:20 - 14:50", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"15:00 - 16:30 ", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi