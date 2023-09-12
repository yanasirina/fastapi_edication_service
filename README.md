### Как поднять контейнеры в докере в докере:
В файле Makeup прописаны команды docker-compose

Поднять:
```console
make up
```
Сбросить:
```console
make down
```
<a href="https://habr.com/ru/companies/first/articles/592321/">Статья на хабре с базовым объяснением команд docker-compose</a>

### Установка зависимостей
```console
pip install -r requirements.txt
```

### Миграции
Для накатывания миграций, если файла alembic.ini ещё нет, нужно запустить в терминале команду:

```
alembic init migrations
```

После этого будет создана папка с миграциями и конфигурационный файл для алембика.

- В alembic.ini нужно задать адрес базы данных, в которую будем катать миграции.
  (Например, postgresql://postgres:postgres@0.0.0.0:5433/postgres)
- Дальше идём в папку с миграциями и открываем env.py, там вносим изменения в блок, где написано

ДО:
```
#from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None
```
ПОСЛЕ:
```
from db.models import Base
target_metadata = Base.metadata
# target_metadata = None
```

- Дальше вводим: ```alembic revision --autogenerate -m "comment"```
- Будет создана миграция
- Дальше вводим: ```alembic upgrade heads```

### Настройка линтера, pre-commit

```
pre-commit install
```
```
pre-commit run --all-files
```
Для отмены прекоммитов:
```
pre-commit uninstall

```
