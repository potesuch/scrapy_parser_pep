# Проект Scrapy для парсинга PEP

Этот проект Scrapy предназначен для парсинга и анализа данных PEP (Python Enhancement Proposals) с сайта [peps.python.org](https://peps.python.org/).

## Установка

1. Убедитесь, что у вас установлен Python 3.7 или новее.
2. Установите виртуальное окружение (опционально, но рекомендуется):
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
    ```
3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

## Использование

Для запуска паука используйте следующую команду:
```sh
scrapy crawl pep
```

После завершения работы паука будет создан CSV-файл с названием status_summary_<дата_время>.csv в директории results. Этот файл содержит сводку по статусам PEP и общее количество собранных PEP.
