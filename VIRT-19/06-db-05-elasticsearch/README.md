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
![Снимок экрана от 2022-10-30 17-59-51](https://user-images.githubusercontent.com/103331839/198886307-a8af93e7-3d46-4c12-8847-6d85666baa75.png)

```bash
┌─(~/GIT/my_rep_netology/devops-19/VIRT-19/06-db-05-elasticsearch)──────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(18:23:48 on main ✚ ✭)──> sudo docker push netology_elastic:v1                                                                                                                  1 ↵ ──(Вс,окт30)─┘
The push refers to repository [docker.io/library/netology_elastic]
d7000fe19fc8: Preparing 
8bd1bd5093f3: Preparing 
a5bda59a0fc7: Preparing 
174f56854903: Preparing 
denied: requested access to the resource is denied
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
