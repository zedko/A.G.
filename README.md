# Test task


## Как развернуть?
* Clone this repo  
* make virtualenv with python 3.9.0 and activate it. Then go to project folder  
* `pip install -r requirements.txt`  
* `cd project`
* `python project/manage.py migrate`  
* `python project/manage.py createsuperuser --username django --email test@test.ru`  
* input your password two times  
* `python project/manage.py runserver`  


## По архитектуре:
1) Задача не очень большая, все можно было реализовать в одном django app.  
2) Старался использовать готовые решения, где это возможно. Т.к. это выгодно.  
3) Вынес secret keys в отдельный файлик, что бы вам проще было развернуть. Но, конечно, лучше для этого использовать ENV VARS  


## По задачам:

1. Необходимо подключить библиотеку [Bootstrap](https://getbootstrap.com) и использовать её для всех view's  
   - Done (via CDN)  
2. Все изменения с описаниями комитить на GIT (Github/Bitbucket/etc)  
   - Done  
3. Сделать окошко логина по Имени/Паролю  
   - Done. Доступно только незалогиненому пользователю. url = /auth/login/, также это индексная страничка.  
4. Форму сброса пароля по Email  
   - Done. !!! Ссылка приходит в консоль !!! Использовал для задания стандартное поле email для auth.models.User, оно не подойдет для реального продукта. url = /auth/reset_password/  
5. Сделать окошко регистрации с полями Имя, Пароль, Email, Телефон, Google капча. После сабмита формы создается запись пользователя и происходит редирект в панельку  
   - Done. Ссылка на есть на странице логина. url = /auth/registration/  
6. При неподтвержденном Email вверху панели висит плашка о необходимости подтвердить Email  
   - Done. В модели authapp Profile есть boolean field. У всех по-умолчанию неподтвержен. Механизм подтверждения не реализовывал. Сделал строго по задаче.  
7. В панели сделать кнопку генерации и отображения секрет ключа для доступа к API  
   - Done  
8. Сделать метод REST API по запросу с секрет ключом, которая просто отдает имя и email аккаунта.  
   - Done. url = /api/method/ . Запрос отдается по методу GET на url. Токен надо предать как HTTP заголовок -> key=Authorization, value=Token [token]   
9. Для админ аккаунта в панели сделать список всех пользователей с возможностью их редактировать и удалять  
   - Done  
10. Для админ аккаунта сделать список с историей всех запросов к REST API  
    - Done. Реализовал через middleware  
11. Для всех пользователей в navbar'e сделать возможность сделать logout  
    - Done  
