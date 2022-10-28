# Домашнее задание к занятию "6.4. PostgreSQL"

## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume.

Подключитесь к БД PostgreSQL используя `psql`.

Воспользуйтесь командой `\?` для вывода подсказки по имеющимся в `psql` управляющим командам.

**Найдите и приведите** управляющие команды для:
- вывода списка БД
- подключения к БД
- вывода списка таблиц
- вывода описания содержимого таблиц
- выхода из psql

## Ответ
```bash
┌─(~/GIT/my_rep_netology/devops-19/VIRT-19/06-db-04-postgresql)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(22:39:58 on main ✹ ✚ ✭)──> sudo docker pull postgres:13 
....
Digest: sha256:2b31dc28ab2a687bb191e66e69c2534c9c74107ddb3192ff22a04de386425905
Status: Downloaded newer image for postgres:13
docker.io/library/postgres:13

┌─(~/GIT/my_rep_netology/devops-19/VIRT-19/06-db-04-postgresql)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(22:44:55 on main ✹ ✚ ✭)──> sudo docker volume create psql_volume                                                                                                                       1 ↵ ──(Пт,окт28)─┘
psql_volume

┌─(~/GIT/my_rep_netology/devops-19/VIRT-19/06-db-04-postgresql)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(22:45:01 on main ✹ ✚ ✭)──> sudo docker run --name psql_docker -e POSTGRES_PASSWORD=t0hab -d -p 5432:5432 -v psql_postgres:/var/lib/postgresql/data postgres:13                             ──(Пт,окт28)─┘
a97bc4846222d7a8484cd1c1e05924132d4be6868eb55e854c9bd62ae2ecbe03
```

```sql
--вывода списка БД
postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)

--подключения к БД
postgres=# \c postgres
Password: 
You are now connected to database "postgres" as user "postgres".

--вывода списка таблиц
postgres=# \dt
Did not find any relations.
postgres=# \dtS
                    List of relations
   Schema   |          Name           | Type  |  Owner   
------------+-------------------------+-------+----------
 pg_catalog | pg_aggregate            | table | postgres
 pg_catalog | pg_am                   | table | postgres
 pg_catalog | pg_amop                 | table | postgres
 pg_catalog | pg_amproc               | table | postgres
 pg_catalog | pg_attrdef              | table | postgres
 pg_catalog | pg_attribute            | table | postgres
 pg_catalog | pg_auth_members         | table | postgres
 pg_catalog | pg_authid               | table | postgres
 pg_catalog | pg_cast                 | table | postgres
 pg_catalog | pg_class                | table | postgres
 pg_catalog | pg_collation            | table | postgres
 pg_catalog | pg_constraint           | table | postgres

--вывода описания содержимого таблиц
postgres=# \dS+
                                            List of relations
   Schema   |              Name               | Type  |  Owner   | Persistence |    Size    | Description 
------------+---------------------------------+-------+----------+-------------+------------+-------------
 pg_catalog | pg_aggregate                    | table | postgres | permanent   | 56 kB      | 
 pg_catalog | pg_am                           | table | postgres | permanent   | 40 kB      | 
 pg_catalog | pg_amop                         | table | postgres | permanent   | 80 kB      | 
 pg_catalog | pg_amproc                       | table | postgres | permanent   | 64 kB      | 
 pg_catalog | pg_attrdef                      | table | postgres | permanent   | 8192 bytes | 
 pg_catalog | pg_attribute                    | table | postgres | permanent   | 456 kB     | 
 pg_catalog | pg_auth_members                 | table | postgres | permanent   | 40 kB      | 
 pg_catalog | pg_authid                       | table | postgres | permanent   | 48 kB      | 
 pg_catalog | pg_available_extension_versions | view  | postgres | permanent   | 0 bytes    | 
 pg_catalog | pg_available_extensions         | view  | postgres | permanent   | 0 bytes    | 
 pg_catalog | pg_cast                         | table | postgres | permanent   | 48 kB      | 
 pg_catalog | pg_class                        | table | postgres | permanent   | 136 kB     | 

postgres=# \dS+ pg_aggregate
                                   Table "pg_catalog.pg_aggregate"
      Column      |   Type   | Collation | Nullable | Default | Storage  | Stats target | Description 
------------------+----------+-----------+----------+---------+----------+--------------+-------------
 aggfnoid         | regproc  |           | not null |         | plain    |              | 
 aggkind          | "char"   |           | not null |         | plain    |              | 
 aggnumdirectargs | smallint |           | not null |         | plain    |              | 
 aggtransfn       | regproc  |           | not null |         | plain    |              | 
 aggfinalfn       | regproc  |           | not null |         | plain    |              | 
 aggcombinefn     | regproc  |           | not null |         | plain    |              | 
 aggserialfn      | regproc  |           | not null |         | plain    |              | 
 aggdeserialfn    | regproc  |           | not null |         | plain    |              | 
 aggmtransfn      | regproc  |           | not null |         | plain    |              | 
 aggminvtransfn   | regproc  |           | not null |         | plain    |              | 
 aggmfinalfn      | regproc  |           | not null |         | plain    |              | 
 aggfinalextra    | boolean  |           | not null |         | plain    |              | 

--выхода из psql
postgres=# \q
```

## Задача 2

Используя `psql` создайте БД `test_database`.

Изучите [бэкап БД](https://github.com/netology-code/virt-homeworks/tree/master/06-db-04-postgresql/test_data).

Восстановите бэкап БД в `test_database`.

Перейдите в управляющую консоль `psql` внутри контейнера.

Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.

Используя таблицу [pg_stats](https://postgrespro.ru/docs/postgresql/12/view-pg-stats), найдите столбец таблицы `orders` 
с наибольшим средним значением размера элементов в байтах.

**Приведите в ответе** команду, которую вы использовали для вычисления и полученный результат.

## Ответ

```sql
CREATE DATABASE test_database;
[2022-10-28 23:08:59] Connected
postgres.public> CREATE DATABASE test_database
[2022-10-28 23:09:00] completed in 1 s 504 ms
```
```bash
root@a97bc4846222:/var/lib/postgresql/data# psql -U postgres -f ./test_dump.sql test_database
```
```sql
postgres=# \c test_database
Password: 
You are now connected to database "test_database" as user "postgres".
```
```sql
test_database=# ANALYZE public.orders;
ANALYZE
test_database=# ANALYZE VERBOSE public.orders;
INFO:  analyzing "public.orders"
INFO:  "orders": scanned 1 of 1 pages, containing 8 live rows and 0 dead rows; 8 rows in sample, 8 estimated total rows
ANALYZE
```

## Задача 3

Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и
поиск по ней занимает долгое время. Вам, как успешному выпускнику курсов DevOps в нетологии предложили
провести разбиение таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499).

Предложите SQL-транзакцию для проведения данной операции.

Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?

## Задача 4

Используя утилиту `pg_dump` создайте бекап БД `test_database`.

Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца `title` для таблиц `test_database`?