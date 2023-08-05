### Как поднять контейнеры в докере в докере: 
1. docker-compose сама команда
2. флаг -f используется для обозначения конфигурационного файла и его расположения
3. up используется для поднятия контейнера 
4. флаг -d используется для запуска контейнера в фоновом режиме
```console
docker-compose -f docker-compose-local.yaml up -d
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
  (Например, postgresql+asyncpg://postgres:postgres@0.0.0.0:5433/postgres)
- Дальше идём в папку с миграциями и открываем env.py, там вносим изменения в блок, где написано 

ДО:
```
#from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None
```
ПОСЛЕ:
```
from main import Base
target_metadata = Base.metadata
# target_metadata = None
```

- Дальше вводим: ```alembic revision --autogenerate -m "comment"```
- Будет создана миграция
- Дальше вводим: ```alembic upgrade heads```
