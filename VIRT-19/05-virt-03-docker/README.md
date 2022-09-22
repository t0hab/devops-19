
# Домашнее задание к занятию "5.3. Введение. Экосистема. Архитектура. Жизненный цикл Docker контейнера"

## Задача 1

Сценарий выполения задачи:

- создайте свой репозиторий на https://hub.docker.com;
- выберете любой образ, который содержит веб-сервер Nginx;
- создайте свой fork образа;
- реализуйте функциональность:
запуск веб-сервера в фоне с индекс-страницей, содержащей HTML-код ниже:
```
<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m DevOps Engineer!</h1>
</body>
</html>
```
Опубликуйте созданный форк в своем репозитории и предоставьте ответ в виде ссылки на https://hub.docker.com/username_repo.

### Ответ

https://hub.docker.com/r/t0hab/network_netology

---

## Задача 2

Посмотрите на сценарий ниже и ответьте на вопрос:
"Подходит ли в этом сценарии использование Docker контейнеров или лучше подойдет виртуальная машина, физическая машина? Может быть возможны разные варианты?"

Детально опишите и обоснуйте свой выбор.

--

Сценарий:

- Высоконагруженное монолитное java веб-приложение;
- Nodejs веб-приложение;
- Мобильное приложение c версиями для Android и iOS;
- Шина данных на базе Apache Kafka;
- Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;
- Мониторинг-стек на базе Prometheus и Grafana;
- MongoDB, как основное хранилище данных для java-приложения;
- Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.

### Ответ

2

---

## Задача 3

- Запустите первый контейнер из образа ***centos*** c любым тэгом в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера;
- Запустите второй контейнер из образа ***debian*** в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера;
- Подключитесь к первому контейнеру с помощью ```docker exec``` и создайте текстовый файл любого содержания в ```/data```;
- Добавьте еще один файл в папку ```/data``` на хостовой машине;
- Подключитесь во второй контейнер и отобразите листинг и содержание файлов в ```/data``` контейнера.


### Ответ

```bash
┌─(~)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:40:44)──> sudo docker pull centos                              ──(Чт,сен22)─┘
Using default tag: latest
latest: Pulling from library/centos
a1d0c7532777: Pull complete 
Digest: sha256:a27fd8080b517143cbbbab9dfb7c8571c40d67d534bbdee55bd6c473f432b177
Status: Downloaded newer image for centos:latest
docker.io/library/centos:latest
┌─(~)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:41:03)──> sudo docker ps -a                                    ──(Чт,сен22)─┘
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
┌─(~)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:41:15)──> sudo docker run -t -d --name centos_netology -v  /root/data:/share/data centos
85297bca21da812356ca96a0334ff826450dec7e4b0f87285fdf2a61adcaf6fc
┌─(~)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:42:38)──> sudo docker pull debian                              ──(Чт,сен22)─┘
Using default tag: latest
latest: Pulling from library/debian
23858da423a6: Pull complete 
Digest: sha256:3e82b1af33607aebaeb3641b75d6e80fd28d36e17993ef13708e9493e30e8ff9
Status: Downloaded newer image for debian:latest
docker.io/library/debian:latest
┌─(~)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:42:59)──> sudo docker run -t -d --name debian_netology -v /root/data:/data debian:latest
dffa8170c188256bfad0ea5c214d775a6093c0a1c1a9ad7c301a33398d4d9517
┌─(~)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:43:44)──> sudo docker exec -it centos_netology bash            ──(Чт,сен22)─┘
[root@85297bca21da /]# echo 'centos text' > /share/data/centos.txt
[root@85297bca21da /]# exit
exit
┌─(~)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:44:51)──> echo 'my text' > data/my.txt                         ──(Чт,сен22)─┘
zsh: Нет такого файла или каталога: data/my.txt
┌─(~)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:45:33)──> cd ...                                           1 ↵ ──(Чт,сен22)─┘
┌─(/)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:45:44)──> mkdir data                                           ──(Чт,сен22)─┘
mkdir: невозможно создать каталог «data»: Отказано в доступе
┌─(/)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:45:51)──> sudo mkdir data                                  1 ↵ ──(Чт,сен22)─┘
┌─(/)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:45:58)──> echo 'my text' > data/my.txt                         ──(Чт,сен22)─┘
zsh: Отказано в доступе: data/my.txt
┌─(/)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:46:04)──> sudo echo 'my text' > data/my.txt                1 ↵ ──(Чт,сен22)─┘
zsh: Отказано в доступе: data/my.txt
┌─(/)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:46:18)──> sudo -i                                          1 ↵ ──(Чт,сен22)─┘
t0hab-pc# echo 'my text' > data/my.txt
t0hab-pc# ls
data
t0hab-pc# exit
┌─(/)──────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/0)─┐
└─(14:56:39)──> sudo docker exec -it debian_netology bash            ──(Чт,сен22)─┘
root@dffa8170c188:/# ls data
centos.txt  my.txt
root@dffa8170c188:/# cat data/centos.txt data/my.txt
centos text
my text
root@dffa8170c188:/# ```
```

---

## Задача 4 (*)

Воспроизвести практическую часть лекции самостоятельно.

Соберите Docker образ с Ansible, загрузите на Docker Hub и пришлите ссылку вместе с остальными ответами к задачам.


### Ответ

4
---