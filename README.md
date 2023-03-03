# Тестовое задание для стажера Python

Необходимо написать очень простой поисковик по текстам документов. Данные хранятся в БД по желанию, поисковый индекс в эластике. 

Ссылка на тестовый массив данных: [[csv](https://disk.yandex.ru/d/HF1iDIN7DXqNVQ)]

### Структура БД:

- `id` - уникальный для каждого документа;
- `rubrics` - массив рубрик;
- `text` - текст документа;
- `created_date` - дата создания документа.

### Структура Индекса:

- `iD` - id из базы;
- `text` - текст из структуры БД.

## Необходимые методы

- сервис должен принимать на вход произвольный текстовый запрос, искать по тексту документа в индексе и возвращать первые 20 документов со всем полями БД, упорядоченные по дате создания;
- удалять документ из БД и индекса по полю  `id`.

## Технические требования:

- любой python фреймворк кроме Django и DRF;
- `README` с гайдом по поднятию;
- `docs.json` - документация к сервису в формате openapi.

## Программа максимум:

- функциональные тесты;
- сервис работает в Docker;
- асинхронные вызовы.
<h1 align="center">Развертывание проекта</h1>
<h4>1. Скачать проект</h4>
  


```
    git clone git@github.com:A-V-tor/test-task-es.git
```

<h4>2. Создать виртуальное окружение и установить зависимости</h4>


```
    cd test-task-es
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
```
Или в случае использования <b>poetry</b>
```
    poetry shell
    poetry install
```
<h4>3. Установить elasticsearch https://www.elastic.co/downloads/past-releases/elasticsearch-8-6-2 и распаковать архив </h4>


```
    vim elasticsearch-8.6.2/config/elasticsearch.yml
```
Установить значение `false` для `xpack.security.enabled: false` </br>
Запуск elasticsearch </br>
```
    cd elasticsearch-8.6.2
    ./bin/elasticsearch
```
Убедиться в работе сервиса `http://localhost:9200/` </br>
<h4>4. Скачать posts.csv в корень проекта </h4>
<h4>5. Подготовить бд и индекс для работы</h4>

```
    cd test-task-es
    python3 -i fill.py
```
Вызвать функцию `fill_data_base()` и дождаться ответа `OK` </br></br>
<i>бд и индекс наполнятся данными, это займет какое - то время</i> </br>
<h4>6. Запуск проекта </h4>

```
    gunicorn -w 3 -b 0.0.0.0:5000 app:app
```

`http://127.0.0.1:5000/` - страница визуального отображения бд  </br></br>
Документация по адресу `http://127.0.0.1:5000/swagger-ui`

<h4>7. Запуск тестов </h4>

`pytest` или `poetry run pytest`

<h3>P.S.</h3>
<i>В качестве фреймворка - flask</i>
