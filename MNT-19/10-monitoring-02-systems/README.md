# Домашнее задание к занятию "13.Системы мониторинга"

## Обязательные задания

1. Вас пригласили настроить мониторинг на проект. На онбординге вам рассказали, что проект представляет из себя 
платформу для вычислений с выдачей текстовых отчетов, которые сохраняются на диск. Взаимодействие с платформой 
осуществляется по протоколу http. Также вам отметили, что вычисления загружают ЦПУ. Какой минимальный набор метрик вы
выведите в мониторинг и почему?

- Ответ:
  
  ЦПУ, ОЗУ, место на диске, сеть - мониторинг основных используемых приложением показателей загруженности системы

  Состояние службы веб-сервера, статуса и времени ответа на http-запрос - контроль состояния интерфейса для работы с платформой.

#
2. Менеджер продукта посмотрев на ваши метрики сказал, что ему непонятно что такое RAM/inodes/CPUla. Также он сказал, 
что хочет понимать, насколько мы выполняем свои обязанности перед клиентами и какое качество обслуживания. Что вы 
можете ему предложить?

- Ответ:
  
  Метрики можно обозвать как захочешь, либо научить менеджера понимать что такое RAM, ЦПУ и тд.

  Построить формулу к нужному ему KPI и собирать с помощью метрик эти показатели. К примеру доступность сети, процент ошибок на машине и доступность самой тачки.

  Так же все это можно настроить через оповещение в телеграм. Менеджер таким образом будет ввсегда знать когда случился сбой и когда все полечили. 


#
3. Вашей DevOps команде в этом году не выделили финансирование на построение системы сбора логов. Разработчики в свою 
очередь хотят видеть все ошибки, которые выдают их приложения. Какое решение вы можете предпринять в этой ситуации, 
чтобы разработчики получали ошибки приложения?

Передать ответственность на разработчиков, максимум подсказать как можно настроить мониторинг ошибок через кибана и тд. Лишнию работу тоже не стоит делать, могут на шею сесть, а вышестоящие люди увидят что вы готовы и за бесплатно поработать.

#
4. Вы, как опытный SRE, сделали мониторинг, куда вывели отображения выполнения SLA=99% по http кодам ответов. 
Вычисляете этот параметр по следующей формуле: summ_2xx_requests/summ_all_requests. Данный параметр не поднимается выше 
70%, но при этом в вашей системе нет кодов ответа 5xx и 4xx. Где у вас ошибка?

- Ответ:
  
  Не учтены коды ответов (3хх)

#
5. Опишите основные плюсы и минусы pull и push систем мониторинга.

- Ответ:
  
  PULL Плюсы: Простота - отправляем запрос и получаем ответ. Не получили ответ - что-то работает не так. Минусы: Отправка запросов на получение ответа - увеличение трафика.
  
  PUSH Плюсы: Меньше трафика т.к. сразу отправляется информация. Минусы: Не везде применим. Например, snmp.



#
1. Какие из ниже перечисленных систем относятся к push модели, а какие к pull? А может есть гибридные?

    Prometheus - pull
    TICK - push
    Zabbix - push/pull
    VictoriaMetrics - push/pull
    Nagios - pull
#
1. Склонируйте себе [репозиторий](https://github.com/influxdata/sandbox/tree/master) и запустите TICK-стэк, 
используя технологии docker и docker-compose.

В виде решения на это упражнение приведите выводы команд с вашего компьютера (виртуальной машины):

    - curl http://localhost:8086/ping
    - curl http://localhost:8888
    - curl http://localhost:9092/kapacitor/v1/ping

А также скриншот веб-интерфейса ПО chronograf (`http://localhost:8888`). 

P.S.: если при запуске некоторые контейнеры будут падать с ошибкой - проставьте им режим `Z`, например
`./data:/var/lib:Z`

- Ответ:

```bash
  [+] Running 6/6
 ⠿ Network sandbox_default            Created                                                                                                                                0.0s
 ⠿ Container sandbox-influxdb-1       Started                                                                                                                                4.6s
 ⠿ Container sandbox-documentation-1  Started                                                                                                                                0.6s
 ⠿ Container sandbox-kapacitor-1      Started                                                                                                                                4.7s
 ⠿ Container sandbox-telegraf-1       Started                                                                                                                                4.8s
 ⠿ Container sandbox-chronograf-1     Started                                                                                                                                5.0s
Opening tabs in browser...
MacBook-Air-Tokhir:sandbox root#
```

```bash
Last login: Mon Feb 27 00:06:47 on ttys002
❯ curl http://localhost:8086/ping
❯ curl http://localhost:8888
<!DOCTYPE html><html><head><link rel="stylesheet" href="/index.c708214f.css"><meta http-equiv="Content-type" content="text/html; charset=utf-8"><title>Chronograf</title><link rel="icon shortcut" href="/favicon.70d63073.ico"></head><body> <div id="react-root" data-basepath=""></div> <script type="module" src="/index.e81b88ee.js"></script><script src="/index.a6955a67.js" nomodule="" defer></script> </body></html>%
❯ curl http://localhost:9092/kapacitor/v1/ping
  ~
❯
```  

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/221432032-e6a2d67b-15d0-421a-9283-446d63d833b7.png">



#
8. Перейдите в веб-интерфейс Chronograf (`http://localhost:8888`) и откройте вкладку `Data explorer`.

    - Нажмите на кнопку `Add a query`
    - Изучите вывод интерфейса и выберите БД `telegraf.autogen`
    - В `measurments` выберите mem->host->telegraf_container_id , а в `fields` выберите used_percent. 
    Внизу появится график утилизации оперативной памяти в контейнере telegraf.
    - Вверху вы можете увидеть запрос, аналогичный SQL-синтаксису. 
    Поэкспериментируйте с запросом, попробуйте изменить группировку и интервал наблюдений.

Для выполнения задания приведите скриншот с отображением метрик утилизации места на диске 
(disk->host->telegraf_container_id) из веб-интерфейса.

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/221432765-6baf1536-e112-4a98-ba7d-28348d964045.png">


#
9. Изучите список [telegraf inputs](https://github.com/influxdata/telegraf/tree/master/plugins/inputs). 
Добавьте в конфигурацию telegraf следующий плагин - [docker](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/docker):
```
[[inputs.docker]]
  endpoint = "unix:///var/run/docker.sock"
```

Дополнительно вам может потребоваться донастройка контейнера telegraf в `docker-compose.yml` дополнительного volume и 
режима privileged:
```
  telegraf:
    image: telegraf:1.4.0
    privileged: true
    volumes:
      - ./etc/telegraf.conf:/etc/telegraf/telegraf.conf:Z
      - /var/run/docker.sock:/var/run/docker.sock:Z
    links:
      - influxdb
    ports:
      - "8092:8092/udp"
      - "8094:8094"
      - "8125:8125/udp"
```
После настройке перезапустите telegraf, обновите веб интерфейс и приведите скриншотом список `measurments` в 
веб-интерфейсе базы telegraf.autogen . Там должны появиться метрики, связанные с docker.

- Ответ:
<img width="1174" alt="image" src="https://user-images.githubusercontent.com/103331839/221434654-c65c314c-b48d-4b24-aa97-c851dd69ea6d.png">
