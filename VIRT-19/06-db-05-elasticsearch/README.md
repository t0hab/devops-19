# Домашнее задание к занятию "6.5. Elasticsearch"

## Задача 1

В этом задании вы потренируетесь в:
- установке elasticsearch
- первоначальном конфигурировании elastcisearch
- запуске elasticsearch в docker

Используя докер образ [elasticsearch:7](https://hub.docker.com/_/elasticsearch) как базовый:

- составьте Dockerfile-манифест для elasticsearch
- соберите docker-образ и сделайте `push` в ваш docker.io репозиторий
- запустите контейнер из получившегося образа и выполните запрос пути `/` c хост-машины

Требования к `elasticsearch.yml`:
- данные `path` должны сохраняться в `/var/lib` 
- имя ноды должно быть `netology_test`

В ответе приведите:
- текст Dockerfile манифеста
- ссылку на образ в репозитории dockerhub
- ответ `elasticsearch` на запрос пути `/` в json виде

Подсказки:
- при сетевых проблемах внимательно изучите кластерные и сетевые настройки в elasticsearch.yml
- при некоторых проблемах вам поможет docker директива ulimit
- elasticsearch в логах обычно описывает проблему и пути ее решения
- обратите внимание на настройки безопасности такие как `xpack.security.enabled` 
- если докер образ не запускается и падает с ошибкой 137 в этом случае может помочь настройка `-e ES_HEAP_SIZE`
- при настройке `path` возможно потребуется настройка прав доступа на директорию

Далее мы будем работать с данным экземпляром elasticsearch.

### Ответ
```bash
┌─(~/GIT/my_rep_netology/devops-19/VIRT-19/06-db-05-elasticsearch)──────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/2)─┐
└─(17:51:01 on main ✹ ✚ ✭)──> sudo docker build -t netology_elastic:v1 .  
...
Successfully built 0fde4817cdad
Successfully tagged netology_elastic:v1
(~/GIT/my_rep_netology/devops-19/VIRT-19/06-db-05-elasticsearch)──────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/2)─┐
└─(17:53:00 on main ✹ ✚ ✭)──> sudo docker run --name elastic -p 9200:9200 -p 9300:9300 -d netology_elastic:v1                                                                         ──(Вс,окт30)─┘
be0a9c6db8a82542c8322c339ec7e5305df313c62fb5b0ac99115999516c10b1
```


```bash
┌─(~/GIT/my_rep_netology/devops-19/VIRT-19/06-db-05-elasticsearch)──────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(18:32:42 on main ✹ ✚ ✭)──> sudo docker push t0hab/netology_elastic:v1                                                                                                          1 ↵ ──(Вс,окт30)─┘
The push refers to repository [docker.io/t0hab/netology_elastic]
d7000fe19fc8: Pushing [===========>                                       ]  120.5MB/517.7MB
8bd1bd5093f3: Pushed 
a5bda59a0fc7: Pushing [====>                                              ]  82.18MB/838.7MB
174f56854903: Pushing [================>                                  ]  66.64MB/203.9MB

```
https://hub.docker.com/repository/docker/t0hab/netology_elastic

## Задача 2

В этом задании вы научитесь:
- создавать и удалять индексы
- изучать состояние кластера
- обосновывать причину деградации доступности данных

Ознакомтесь с [документацией](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html) 
и добавьте в `elasticsearch` 3 индекса, в соответствии со таблицей:

| Имя | Количество реплик | Количество шард |
|-----|-------------------|-----------------|
| ind-1| 0 | 1 |
| ind-2 | 1 | 2 |
| ind-3 | 2 | 4 |

Получите список индексов и их статусов, используя API и **приведите в ответе** на задание.

Получите состояние кластера `elasticsearch`, используя API.

Как вы думаете, почему часть индексов и кластер находится в состоянии yellow?

Удалите все индексы.

**Важно**

При проектировании кластера elasticsearch нужно корректно рассчитывать количество реплик и шард,
иначе возможна потеря данных индексов, вплоть до полной, при деградации системы.

```bash
curl -X PUT localhost:9200/ind-1 -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 1,  "number_of_replicas": 0 }}'
curl -X PUT localhost:9200/ind-2 -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 2,  "number_of_replicas": 1 }}'
curl -X PUT localhost:9200/ind-3 -H 'Content-Type: application/json' -d'{ "settings": { "number_of_shards": 4,  "number_of_replicas": 2 }}'    
```
```bash
┌─(~/GIT/my_rep_netology)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(19:57:53)──> curl -X GET 'http://localhost:9200/_cat/indices?v'                                                                                                                        127 ↵ ──(Пн,окт31)─┘

health status index            uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   .geoip_databases PeGHR1QqRaqxGPpVye4gzQ   1   0         41           38     39.1mb         39.1mb
green  open   ind-1            oDCLH2xBQXSnXnHUfunywQ   1   0          0            0       226b           226b
yellow open   ind-3            lc8DwcMwTmeZAcbAKXTWwQ   4   2          0            0       904b           904b
yellow open   ind-2            zij0GALYRZKE2gL1xwXGUA   2   1          0            0       452b           452b

```
```bash
┌─(~/GIT/my_rep_netology)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(19:58:06)──> curl -X GET 'http://localhost:9200/_cluster/health/ind-1?pretty'                                                                                                                ──(Пн,окт31)─┘
{
  "cluster_name" : "es_cluster",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 1,
  "active_shards" : 1,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 100.0
}
┌─(~/GIT/my_rep_netology)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(19:59:16)──> curl -X GET 'http://localhost:9200/_cluster/health/ind-2?pretty'                                                                                                                ──(Пн,окт31)─┘
{
  "cluster_name" : "es_cluster",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 2,
  "active_shards" : 2,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 2,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 44.44444444444444
}

┌─(~/GIT/my_rep_netology)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(19:59:43)──> curl -X GET 'http://localhost:9200/_cluster/health/ind-3?pretty'                                                                                                                ──(Пн,окт31)─┘
{
  "cluster_name" : "es_cluster",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 4,
  "active_shards" : 4,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 8,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 44.44444444444444
}
```

```bash
┌─(~/GIT/my_rep_netology)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(20:21:59)──> curl -X GET "localhost:9200/_cluster/health?pretty"                                                                                                                             ──(Пн,окт31)─┘
{
  "cluster_name" : "es_cluster",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 8,
  "active_shards" : 8,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 44.44444444444444
}
```
--Как вы думаете, почему часть индексов и кластер находится в состоянии yellow?
Потому что реплика не может находиться с шардом на одном узле. Копия тоже не назначена. Реплицироваться некуда.

--удаление 
```bash
┌─(~/GIT/my_rep_netology)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(20:28:52)──> curl -X DELETE 'http://localhost:9200/_all'                                                                                                                               127 ↵ ──(Пн,окт31)─┘

{"acknowledged":true}%                                                                                                                                                                                         ┌─(~/GIT/my_rep_netology)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(20:28:57)──> curl 'localhost:9200/_cat/indices?v'                                                                                                                                            ──(Пн,окт31)─┘
health status index            uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   .geoip_databases PeGHR1QqRaqxGPpVye4gzQ   1   0         41           38     39.1mb         39.1mb
```

## Задача 3

В данном задании вы научитесь:
- создавать бэкапы данных
- восстанавливать индексы из бэкапов

Создайте директорию `{путь до корневой директории с elasticsearch в образе}/snapshots`.

Используя API [зарегистрируйте](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-register-repository.html#snapshots-register-repository) 
данную директорию как `snapshot repository` c именем `netology_backup`.

**Приведите в ответе** запрос API и результат вызова API для создания репозитория.

Создайте индекс `test` с 0 реплик и 1 шардом и **приведите в ответе** список индексов.

[Создайте `snapshot`](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-take-snapshot.html) 
состояния кластера `elasticsearch`.

**Приведите в ответе** список файлов в директории со `snapshot`ами.

Удалите индекс `test` и создайте индекс `test-2`. **Приведите в ответе** список индексов.

[Восстановите](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-restore-snapshot.html) состояние
кластера `elasticsearch` из `snapshot`, созданного ранее. 

**Приведите в ответе** запрос к API восстановления и итоговый список индексов.

Подсказки:
- возможно вам понадобится доработать `elasticsearch.yml` в части директивы `path.repo` и перезапустить `elasticsearch`