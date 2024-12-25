from PyQt5 import QtCore, QtWidgets, QtCore, QtGui
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from PySide6.QtWidgets import QMessageBox
import sqlite3 as sql
import sys
import inter_rasp
import inter_rasp_stud
import inter_employee
import inter_student
import inter_log

class Shedule_edit(QDialog):
    def __init__(self):
        super(Shedule_edit, self).__init__()
        self.ui = inter_rasp.Ui_Dialog()
        self.ui.setupUi(self)
        self.groups=['Group1','Group2','Group3']
        self.group_number = 1
        self.ui.comboBox.currentIndexChanged.connect(self.update_group_number)
        self.load_data(self.group_number)
        self.ui.pushButton.clicked.connect(lambda: self.save_data(self.group_number))
        self.ui.pushButton_2.clicked.connect(self.exit)


    def update_group_number(self):
        self.group_number = self.ui.comboBox.currentIndex() + 1
        self.clear_textedits()
        self.load_data(self.group_number)

    def clear_textedits(self):
        for i in range(1, 31):
            text_edit = getattr(self.ui, f'textEdit_{i}', None)
            text_edit.clear()

    def load_data(self,group_number):
        group=self.groups[group_number-1]
        connection = sql.connect('Database_rasp.db')
        cursor = connection.cursor()
        cursor.execute('SELECT tt FROM '+group)
        rows = cursor.fetchall()
        for i, (text,) in enumerate(rows):
            if text != '0':
                text_edit = getattr(self.ui, f'textEdit_{i+1}', None)
                if text_edit:
                    text_edit.setPlainText(text)
        connection.close()
      
    def save_data(self,group_number):
        group=self.groups[group_number-1]
        connection = sql.connect('Database_rasp.db')
        cursor = connection.cursor()
        for i in range(1, 31):
            text_edit = getattr(self.ui, f'textEdit_{i}', None)
            if text_edit:
                cursor.execute('UPDATE '+group+' SET tt = ? WHERE id = ?', (text_edit.toPlainText(), i))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Данные успешно сохранены!")
        msg.setWindowTitle("Успех")
        msg.setStyleSheet("background-color: white; color: black;")
        msg.addButton(QMessageBox.Ok)
        msg.exec_()
        connection.commit()
        connection.close()

    def exit(self):
        self.close()

class Shedule_stud(QDialog):
    def __init__(self, Stg):
        super(Shedule_stud, self).__init__()
        self.ui = inter_rasp_stud.Ui_Dialog()
        self.ui.setupUi(self)
        self.groups=['Group1','Group2','Group3']
        self.Stg = Stg
        self.group_number = Stg
        self.load_data(self.group_number)
        self.ui.pushButton_2.clicked.connect(self.exit)

    def load_data(self,group_number):
        group=self.groups[group_number-1]
        connection = sql.connect('Database_rasp.db')
        cursor = connection.cursor()
        cursor.execute('SELECT tt FROM '+group)
        rows = cursor.fetchall()
        for i, (text,) in enumerate(rows):
            if text != '0':
                label = getattr(self.ui, f'label_r_{i+1}', None)
                if label:
                   label.setText(text)
        connection.close()

    def exit(self):
        self.close()

class Emp_menu(QMainWindow):
    def __init__(self):
        super(Emp_menu, self).__init__()
        self.ui = inter_employee.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.window_change_sh_edit)
        self.ui.pushButton_6.clicked.connect(self.window_change_sh_edit)

    def window_change_sh_edit(self):
        self.hide()
        form = Shedule_edit()
        form.exec_()
        self.show()

class Stud_menu(QMainWindow):
    def __init__(self, Stg):
        super(Stud_menu, self).__init__()
        self.ui = inter_student.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(self.window_change_sh_view)
        self.Stg = Stg

    def window_change_sh_view(self):
        self.hide()
        form = Shedule_stud(self.Stg)
        form.exec_()
        self.show()

class Log_menu(QMainWindow):
    def __init__(self):
        super(Log_menu, self).__init__()
        self.ui = inter_log.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.window_changer)
        self.stud_menu_instance = None
        self.emp_menu_instance = None
        self.students_pass = {"Student1": "1111", "Student2": "2222", "Student3": "3333"}
        self.professors_pass = {"Prof1": "1111"}
        self.Stg = 1

    def window_changer(self):
        username = self.ui.textEdit.toPlainText()
        password = self.ui.textEdit_2.toPlainText()
        if username in self.students_pass and self.students_pass[username] == password:
            last_char = username[-1]
            default_g = 1
            if last_char == "1":
                self.Stg = 1
            elif last_char == "2":
                self.Stg = 2
            elif last_char == "3":
                self.Stg = 3
            else:
                self.Stg = default_g
            self.hide()
            if not self.stud_menu_instance:
                self.stud_menu_instance = Stud_menu(self.Stg)
            self.stud_menu_instance.show()
        elif username in self.professors_pass and self.professors_pass[username] == password:
            self.hide()
            if not self.emp_menu_instance:
                self.emp_menu_instance = Emp_menu()
            self.emp_menu_instance.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Неверный логин или пароль!")
            msg.setWindowTitle("Ошибка")
            msg.setStyleSheet("background-color: white; color: black;")
            msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Log_menu()
    form.show()
    sys.exit(app.exec())