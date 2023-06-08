Чтобы получить проект, откройте проект, нажмите кнопку Get From VCS
Вставьте в поле url ссылку на гитхаб проекта и выберите папку

После того как получите проект откройте следующее меню
File -> Settings -> Project:eShop -> Python Intepreter
Нажмите кнопку Add Intepreter выберите Add Local Intepreter
в списке выберите Virtualenv Environment (должно быть выбрано по умолчанию)
После этого выберите пункт New и нажмите кнопку OK
После этого PyCharm создаст venv для проекта
Откройте пункт Terminal в нижнем тулбаре, если venv создался и активировался то вы увидете что-то вроде
(venv) PS C:\Users\karli\PycharmProjects\eShop>

далее в терминале
pip install -r requirements.txt

после этого запустите сервер
python manage.py runserver