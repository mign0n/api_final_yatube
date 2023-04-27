# YaTube API

## Описание

Серверный API социальной сети YaTube, созданный с использованием Django и
Django Rest Framework.

## Технологии

- Python v3.9
- Django v3.2
- Django Rest Framework v3.12

## Запуск проекта в dev-режиме

- Склонируйте репозиторий и перейдите в директорию проекта

```shell
git clone https://github.com/mign0n/api_final_yatube.git && cd api_final_yatube
```

- Установите виртуальное окружение, установите зависимости, выполните миграции
с помощью команды:

```shell
make install
```

- Запустите тесты:

```shell
make test
```

- Запустите сервер:

```shell
make run
```

- Перейдите по адресу `127.0.0.1:8000/redoc`. Эта страница содержит
документацию по API.

- С помощью панели администратора Django создайте пользователя c именем <ИМЯПОЛЬЗОВАТЕЛЯ>
и паролем <ВАШСТОЙКИЙПАРОЛЬ>.

- Запросом POST к API по адресу 127.0.0.1:8000/api/v1/jwt/create/
создайте токен. В теле запроса передайте данные для аутентификации, указанные
ранее, при создании пользователя, например:

```shell
curl --header "content-type:application/json" \
--data '{"username":"<ИМЯПОЛЬЗОВАТЕЛЯ>","password":"<ВАШСТОЙКИЙПАРОЛЬ>"}' \
--request POST http://127.0.0.1:8000/api/v1/jwt/create/
```

Примерный ответ:

```text
{"refresh":"<ВАШ-ТОКЕН-ДЛЯ-ОБНОВЛЕНИЯ-ТОКЕНА>", "access":"<ВАШ-ТОКЕН-ДОСТУПА>"}
```

## Примеры запросов

1. Создание публикации (POST /api/v1/posts/)

```shell
curl --header "content-type:application/json" \
--header "authorization: Bearer <ВАШ-ТОКЕН-ДОСТУПА>" \
--data '{"text": "Текст вашей публикации"}' \
--request POST http://127.0.0.1:8000/api/v1/posts/
```

1. Получение списка публикаций (GET /api/v1/posts/)

```shell
curl --header "content-type:application/json" \
--request GET http://127.0.0.1:8000/api/v1/posts/
```

1. Удаление публикации (DELETE /api/v1/posts/{id}/)

```shell
curl --header "content-type:application/json" \
--header "authorization: Bearer <ВАШ-ТОКЕН-ДОСТУПА>" \
--request DELETE http://127.0.0.1:8000/api/v1/posts/1/
```
