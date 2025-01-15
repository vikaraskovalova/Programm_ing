import os
import subprocess

# Путь к базе данных
db_path = "Database_rasp.db"
backup_db_path = "Database_rasp_orig.db"

def backup_database():
    """Создает резервную копию базы данных."""
    if os.path.exists(db_path):
        print(f"Создана резервная копия {db_path} в {backup_db_path}")
        os.rename(db_path, backup_db_path)

def restore_database():
    """Восстанавливает оригинальную базу данных."""
    if os.path.exists(backup_db_path):
        print(f"Удаляем {db_path} и восстанавливаем {backup_db_path} как {db_path}")
        os.remove(db_path)
        os.rename(backup_db_path, db_path)

def run_tests():
    """Запускает тесты с помощью pytest."""
    print("Вам нужно будет нажать кномки Ок на всплывающих окнах\nЗапуск тестов...")
    result = subprocess.run(["pytest", "test_dekanat.py"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    backup_database()  # Создаем резервную копию
    try:
        run_tests()  # Запускаем тесты
    finally:
        restore_database()  # Восстанавливаем оригинальную базу данных
