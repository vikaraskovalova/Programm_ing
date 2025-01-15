
import pytest
from PyQt5 import QtCore, QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from Main import Log_menu, Shedule_edit, Shedule_stud
from PySide6.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow, QAction, qApp
import sqlite3 as sql

@pytest.fixture(scope='session', autouse=True)
def app():
    """Создание экземпляра QApplication для всей сессии тестов."""
    app = QApplication([])
    yield app
    app.quit()  # Уничтожение приложения после всех тестов

@pytest.fixture
def log_menu(qtbot):
    """Создание окна логина для тестов."""
    window = Log_menu()
    qtbot.addWidget(window)
    return window

#Тест на верно введенный пароль студента
def test_login_valid_student(log_menu, qtbot):
    log_menu.ui.textEdit.setPlainText("Student1")
    log_menu.ui.textEdit_2.setPlainText("1111")
    qtbot.mouseClick(log_menu.ui.pushButton, Qt.LeftButton)

    assert log_menu.stud_menu_instance is not None
    assert log_menu.stud_menu_instance.Stg == 1

#Тест на неверно введенный пароль студента
def test_login_invalid_student(log_menu, qtbot):
    log_menu.ui.textEdit.setPlainText("Student1")
    log_menu.ui.textEdit_2.setPlainText("wrong_password")
    qtbot.mouseClick(log_menu.ui.pushButton, Qt.LeftButton)

    assert log_menu.ui.textEdit.toPlainText() == "Student1"
    assert log_menu.ui.textEdit_2.toPlainText() == "wrong_password"
    assert log_menu.emp_menu_instance is None

#Тест на верно введенный пароль преподавателя
def test_login_valid_prof(log_menu, qtbot):
    log_menu.ui.textEdit.setPlainText("Prof1")
    log_menu.ui.textEdit_2.setPlainText("1111")
    qtbot.mouseClick(log_menu.ui.pushButton, Qt.LeftButton)

    assert log_menu.emp_menu_instance is not None

#Тест на неверно введенный пароль преподавателя
def test_login_invalid_prof(log_menu, qtbot):
    log_menu.ui.textEdit.setPlainText("Prof1")
    log_menu.ui.textEdit_2.setPlainText("wrong_password")
    qtbot.mouseClick(log_menu.ui.pushButton, Qt.LeftButton)

    assert log_menu.ui.textEdit.toPlainText() == "Prof1"
    assert log_menu.ui.textEdit_2.toPlainText() == "wrong_password"
    assert log_menu.stud_menu_instance is None

@pytest.fixture
def setup_database():
    """Создание тестовой базы данных."""
    connection = sql.connect('Database_rasp.db')
    cursor = connection.cursor()
    
    # Создаем таблицы и вставляем тестовые данные
    cursor.execute('CREATE TABLE IF NOT EXISTS Group1 (id INTEGER PRIMARY KEY, tt TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Group2 (id INTEGER PRIMARY KEY, tt TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Group3 (id INTEGER PRIMARY KEY, tt TEXT)')
    
    # Вставляем тестовые данные
    cursor.executemany('INSERT INTO Group1 (tt) VALUES (?)', [(f'Data1_{i}',) for i in range(1, 6)])
    cursor.executemany('INSERT INTO Group2 (tt) VALUES (?)', [(f'Data2_{i}',) for i in range(1, 6)])
    cursor.executemany('INSERT INTO Group3 (tt) VALUES (?)', [(f'Data3_{i}',) for i in range(1, 6)])
    
    connection.commit()
    yield
    # Удаляем таблицы после тестов
    cursor.execute('DROP TABLE IF EXISTS Group1')
    cursor.execute('DROP TABLE IF EXISTS Group2')
    cursor.execute('DROP TABLE IF EXISTS Group3')
    connection.commit()
    connection.close()

def test_load_data_shedule_edit(qtbot, setup_database):
    """Тестирование функции load_data в Shedule_edit."""
    form = Shedule_edit()
    qtbot.addWidget(form)

    form.load_data(1)  # Загружаем данные для Group1

    # Проверяем, что текстовые поля загружены правильно
    for i in range(1, 6):
        text_edit = getattr(form.ui, f'textEdit_{i}', None)
        assert text_edit is not None
        assert text_edit.toPlainText() == f'Data1_{i}'

def test_load_data_shedule_stud(qtbot, setup_database):
    """Тестирование функции load_data в Shedule_stud."""
    form = Shedule_stud(1)  # Создаем экземпляр с группой 1
    qtbot.addWidget(form)

    form.load_data(1)  # Загружаем данные для Group1

    # Проверяем, что метки загружены правильно
    for i in range(1, 6):
        label = getattr(form.ui, f'label_r_{i}', None)
        assert label is not None
        assert label.text() == f'Data1_{i}'

def test_save_data_shedule_edit(qtbot, setup_database):
    """Тестирование функции save_data в Shedule_edit."""
    form = Shedule_edit()
    qtbot.addWidget(form)

    form.load_data(1)  # Загружаем данные для Group1

    # Изменяем данные в текстовых полях
    for i in range(1, 6):
        text_edit = getattr(form.ui, f'textEdit_{i}', None)
        text_edit.setPlainText(f'NewData1_{i}')

    form.save_data(1)  # Сохраняем данные для Group1

    # Проверяем, что данные были сохранены в базе данных
    connection = sql.connect('Database_rasp.db')
    cursor = connection.cursor()
    cursor.execute('SELECT tt FROM Group1 ORDER BY id')
    rows = cursor.fetchall()
    
    for i, (text,) in enumerate(rows):
        assert text == f'NewData1_{i + 1}'

    connection.close()

if __name__ == "__main__":
    pytest.main()
