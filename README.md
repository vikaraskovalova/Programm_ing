# Programm_ing
Информационная система "Деканат"
# README.md

# Расписание (Shedule Manager)

## Описание

Это приложение для управления расписанием, написанное на Python с использованием библиотек PyQt5 и PySide6. Программа предоставляет интерфейс для студентов и преподавателей, позволяя им просматривать и редактировать расписание занятий. Данные хранятся в базе данных SQLite.

## Функциональность

- **Вход в систему**: Пользователи могут входить в систему как студенты или преподаватели, используя свои учетные данные.
- **Редактирование расписания**: Преподаватели могут редактировать расписание для различных групп.
- **Просмотр расписания**: Студенты могут просматривать свое расписание.
- **Уведомления**: Приложение предоставляет уведомления об успешном сохранении данных и ошибках входа.

## Установка

1. Убедитесь, что у вас установлен Python 3.x.
2. Установите необходимые библиотеки:
   ```bash
   pip install PyQt5 PySide6
   ```
3. Убедитесь, что у вас есть база данных `Database_rasp.db` в корневом каталоге проекта.

## Запуск приложения

Для запуска приложения выполните следующую команду в терминале:

```bash
python main.py
```

где `main.py` — это файл, содержащий код приложения.

## Структура проекта

- `main.py`: основной файл приложения, содержащий логику и интерфейс.
- `inter_rasp.py`: интерфейс для редактирования расписания.
- `inter_rasp_stud.py`: интерфейс для просмотра расписания студентами.
- `inter_employee.py`: интерфейс для преподавателей.
- `inter_student.py`: интерфейс для студентов.
- `inter_log.py`: интерфейс для логина.

## Использование

1. При запуске приложения откроется окно входа.
2. Введите имя пользователя и пароль:
   - Студенты: 
     - `Student1`: `1111`
     - `Student2`: `2222`
     - `Student3`: `3333`
   - Преподаватели:
     - `Prof1`: `1111`
3. После успешного входа вы будете перенаправлены на соответствующее меню (студента или преподавателя).
4. Преподаватели могут редактировать расписание, выбирая группу из выпадающего списка и нажимая кнопку "Сохранить".
5. Студенты могут просматривать свое расписание, нажав на соответствующую кнопку.

## Примечания

- Убедитесь, что база данных правильно настроена и содержит необходимые таблицы и данные.
- В случае ошибок входа или сохранения данных приложение предоставит соответствующее уведомление.

## Лицензия

Этот проект является открытым и доступен для использования и модификации. Пожалуйста, указывайте источник при использовании кода.

---

Для получения дополнительной информации или вопросов, пожалуйста, обращайтесь к автору проекта.
