# Домашнее задание к занятию 15 «Система сбора логов Elastic Stack»

## Задание 1

Вам необходимо поднять в докере и связать между собой:

- elasticsearch (hot и warm ноды);
- logstash;
- kibana;
- filebeat.

Logstash следует сконфигурировать для приёма по tcp json-сообщений.

Filebeat следует сконфигурировать для отправки логов docker вашей системы в logstash.

В директории [help](./help) находится манифест docker-compose и конфигурации filebeat/logstash для быстрого 
выполнения этого задания.

Результатом выполнения задания должны быть:

- скриншот `docker ps` через 5 минут после старта всех контейнеров (их должно быть 5);

<img width="1422" alt="image" src="https://user-images.githubusercontent.com/103331839/224804584-044296ec-9a41-4480-ada7-c681db201050.png">

- скриншот интерфейса kibana;

<img width="1428" alt="image" src="https://user-images.githubusercontent.com/103331839/224794554-7c41799f-1a20-484a-aa21-163eb6b4b12e.png">


## Задание 2

Перейдите в меню [создания index-patterns  в kibana](http://localhost:5601/app/management/kibana/indexPatterns/create) и создайте несколько index-patterns из имеющихся.

<img width="1048" alt="image" src="https://user-images.githubusercontent.com/103331839/224805044-dfe98265-86c4-4847-81fe-ef47fe84e146.png">

 


 
