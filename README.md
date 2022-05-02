# Проект Yatube (доработка)

+ Настроен эмулятор отправки писем; отправленные письма сохраняются в виде текстовых файлов в директорию /sent_emails. Настроена отправка письма при восстановлении пароля
+ Создано и подключено приложение core. В нём размещён и зарегистрирован фильтр addclass, позволяющий добавлять CSS-класс к тегу шаблона;
создан и зарегистрирован контекст-процессор, добавляющий текущий год на все страницы в переменную {{ year }}
+ Создано и подключено приложение about, в нём созданы статические страницы /about/author/ и /about/tech/. Ссылки на эти страницы добавлены в навигацию сайта.
+ Для всех путей установлены name и namespace.
+ Подключено приложение django.contrib.auth, его urls.py подключен к головному urls.py. 
+ Создано и подключено приложение users, в нём переопределены шаблоны для адресов /auth/login/ (авторизация), /auth/logout/ (выход из аккаунта).
+ Создана страница /auth/signup/ с формой для регистрации пользователей.
+ В приложении posts: создана страница пользователя profile/<username>/. На ней отображаются посты пользователя. Создана отдельная страница поста posts/<post_id>/.
+ Подключен паджинатор, он выводит по десять постов на главную страницу, на страницу профайла, на страницу группы.
+ Создана навигация по разделам.
+ Добавлена возможность публикации постов: в шапку сайта добавлена ссылка «Новая запись», она видна только авторизованным пользователям и ведет на страницу /create/
На странице /create/ создана форма для добавления новой публикации.
+ Добавлена страница редактирования записи с адресом /posts/<post_id>/edit/. Права на редактирование есть только у автора этого поста. Остальные пользователи перенаправляются на страницу просмотра поста. При редактировании поста заголовок «Добавить запись» заменяется на «Редактировать запись»; надпись на кнопке отправки формы  зависит от операции: «Добавить» для новой записи и «Сохранить» — для редактирования.
  
## Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/kh199/api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
  
Запустить проект:
```
python3 manage.py runserver
```
## Технологии
Python 3.7 
Django 2.2.19
