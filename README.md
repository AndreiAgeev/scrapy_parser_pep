# Проект парсинга PEP с использованием фреймворка Scrapy
## Описание:
Парсер, написанный в рамках обучения на платформе Yandex.Practicum.
Проект используется для парсинга документации PEP с использованием фреймворка Scrapy. Парсер собирает данные обо всех документах PEP и сохраняет их в два файла, в папку results:
- **pep_(дата создания).csv** - CSV-файл, содержащий данные в формате "Номер PEP, Название PEP, Статус PEP";
- **status_summary_(дата создания).csv** - CSV-файл, содержащий данные о том, сколько PEP имеют определённый статус, а также общее количество PEP.

## Как запустить парсер на локальной машине:
Клонировать репозиторий и перейти в него:
```
git clone https://github.com/AndreiAgeev/scrapy_parser_pep.git
```
```
cd scrapy_parser_pep/
```
Создать и активировать вирутальное окружение:<br />
*Для Linux:*
```
python3 -m venv .venv
```
```
source env/bin/activate
```
*Для Windows:*
```
python -m venv .venv
```
```
source env/Scripts/activate
```
Установить зависимости из файла requirements.txt:<br />
*Для Linux:*
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
*Для Windows:*
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Перейти в папку pep_parse и запустить парсер:<br />
```
cd pep_parse/
```
```
scrapy crawl pep
```
По завершению работы в текущей директории появится папка results c указанными в описании файлами.
## Авторы:
**Идея и ТЗ** - Yandex.Practicum<br />
**Реализация** - Andrei Ageev (@AndreiAgeev)
