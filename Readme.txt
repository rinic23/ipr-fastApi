1.docker-compose up - команда поднимает контейнеры, pg_admin, postgresql, postgress
2.make migrations_create - создание миграции.
3.make migrations_run - обновления миграций.

2 и 3 команды нужны для изменения структуры БД, и запускаются по порядку: сначала 2 потом 3 