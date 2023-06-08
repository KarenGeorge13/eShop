Чтобы запустить проект, установите виртуальное окружение venv
Для создания виртуального окружения, перейдите в корневую директорию проекта и выполните:
python -m venv venv

Затем активируйте его
venv\Scripts\activate.bat

Установите необходимые проекту пакеты из файла requirements.txt
pip install -r requirements.txt

Проведите миграции
python manage.py migrate

И запустите сервер
python manage.py runserver