## scrapy_parser_pep

### Учебный проект для парсинга сайта https://peps.python.org/ с помощью фреймворка Scrapy.

### Развертывание

Для установки необходимо склонировать репозиторий и установить зависимости:
```
git clone 
```

```
cd yacut
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

- Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

для запуска парсера необходимо выполнить команду `scrapy crawl pep`

Результаты парсинга будут сохранены в директорию `reslts`

### Системные требования
Python >= 3.9 + requirements
