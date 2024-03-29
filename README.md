### Простой RESTful API сервис для реферальной системы.
#### Запуск API в PyCharm:
- Для начала работы скопируйте репозиторий на локальную машину: `git clone https://github.com/Giriraj-das/Referral-RESTful-API`
- Откройте склонированный репозиторий в PyCharm
- Если PyCharm не предложит сам:
  - Создайте виртуальное окружение
  - Установите зависимости: `pip install -r requirements.txt`
- Создать контейнер с PostgreSQL в Docker: `docker run --name stakewolle-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16.2-alpine`
- Применяем миграции `./manage.py migrate`
#### Запуск API в Docker ARM архитектура:
- Скачать yml-файл: https://github.com/Giriraj-das/Referral-RESTful-API/blob/main/docker-compose.yml
- В терминале из директории, где лежит yml-файл запустить: `docker-compose up -d`
- Документация по адресу: http://127.0.0.1:8000/api/docs/
### URLs:
- http://127.0.0.1:8000/api/docs/ Swagger документация


- http://127.0.0.1:8000/user/ вывести список пользователей с подсчетом количества рефералов у каждого. Если добавить в url-адрес id реферера (`/?id=1`), выведет список рефералов.
- http://127.0.0.1:8000/user/create/ создать пользователя. Если добавить в url-адрес реферальный код (`/?code=hv23FDd6`), создаст реферала.
- http://127.0.0.1:8000/user/{id}/delete/ удалить пользователя.
- http://127.0.0.1:8000/user/token/ получить JWT-токен.
- http://127.0.0.1:8000/user/token/refresh/ обновить JWT-токен.


- http://127.0.0.1:8000/ref-code/create/ создать реферальный код. Создается автоматически, нужно ввести только дату и время окончания.
- http://127.0.0.1:8000/ref-code/{id}/delete/ удалить реферальный код.
- http://127.0.0.1:8000/ref-code/get-by-email/ получить реферальный код по email.
