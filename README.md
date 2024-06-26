# YaTube API

[![CI](https://github.com/mign0n/api_final_yatube/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/mign0n/api_final_yatube/actions/workflows/python-app.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://github.com/python/mypy)
[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

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

- Перейдите по адресу `127.0.0.1:8000/api/v1/doc`. Эта страница содержит
интерактивную документацию по API.

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

HTTP-запросы можно отправлять прямо со страницы документации
`127.0.0.1:8000/api/v1/doc`.

Используйте полученный токен в заголовках запросов, либо авторизуйтесь с
помощью кнопки '__Authorize__' на странице документации и введите
`<ВАШ-ТОКЕН-ДОСТУПА>` в поле 'Value'.
