# Домашнее задание к занятию 14 «Средство визуализации Grafana»

## Обязательные задания

### Задание 1

1. Используя директорию [help](./help) внутри этого домашнего задания, запустите связку prometheus-grafana.

<img width="1035" alt="image" src="https://user-images.githubusercontent.com/103331839/224560011-f5c9b45c-b336-47d9-8283-157995ba375b.png">

2. Зайдите в веб-интерфейс grafana, используя авторизационные данные, указанные в манифесте docker-compose.

<img width="1425" alt="image" src="https://user-images.githubusercontent.com/103331839/224560081-3671c031-db96-48b3-a41b-e8c979bd7b13.png">

3. Подключите поднятый вами prometheus, как источник данных.
4. Решение домашнего задания — скриншот веб-интерфейса grafana со списком подключенных Datasource.

<img width="970" alt="image" src="https://user-images.githubusercontent.com/103331839/224562797-6a2f5263-bae2-422c-b0fd-1764dc29d1ab.png">


## Задание 2

Изучите самостоятельно ресурсы:

1. [PromQL tutorial for beginners and humans](https://valyala.medium.com/promql-tutorial-for-beginners-9ab455142085).
1. [Understanding Machine CPU usage](https://www.robustperception.io/understanding-machine-cpu-usage).
1. [Introduction to PromQL, the Prometheus query language](https://grafana.com/blog/2020/02/04/introduction-to-promql-the-prometheus-query-language/).

Создайте Dashboard и в ней создайте Panels:

- утилизация CPU для nodeexporter (в процентах, 100-idle);

<img width="665" alt="image" src="https://user-images.githubusercontent.com/103331839/224563434-5f80aeae-25ba-4070-9ed8-396520445e98.png">

- CPULA 1/5/15;

<img width="663" alt="image" src="https://user-images.githubusercontent.com/103331839/224563846-dd1cc432-ab33-4430-bb74-37f2fa8580d7.png">

- количество свободной оперативной памяти;

<img width="663" alt="image" src="https://user-images.githubusercontent.com/103331839/224564020-4a51c6c6-dcce-4ba8-b558-4868ad134889.png">

- количество места на файловой системе.

<img width="665" alt="image" src="https://user-images.githubusercontent.com/103331839/224564128-4ca7d36b-d7ec-43fa-a4c6-84f707b66bfc.png">


Для решения этого задания приведите promql-запросы для выдачи этих метрик, а также скриншот получившейся Dashboard.

<img width="1423" alt="image" src="https://user-images.githubusercontent.com/103331839/224564181-71d18a1b-a8c4-4cf5-993e-c38b659fa416.png">

avg (rate(node_cpu_seconds_total{instance="nodeexporter:9100", job="nodeexporter", mode="idle"}[10s]) * 100)

node_load1{instance="nodeexporter:9100", job="nodeexporter"}

node_load5{instance="nodeexporter:9100", job="nodeexporter"}

node_load15{instance="nodeexporter:9100", job="nodeexporter"}

avg_over_time (node_memory_MemFree_bytes{instance="nodeexporter:9100", job="nodeexporter"}[20s])

node_filesystem_free_bytes{instance="nodeexporter:9100", job="nodeexporter", mountpoint="/"}


## Задание 3

1. Создайте для каждой Dashboard подходящее правило alert — можно обратиться к первой лекции в блоке «Мониторинг».
1. В качестве решения задания приведите скриншот вашей итоговой Dashboard.

<img width="1349" alt="image" src="https://user-images.githubusercontent.com/103331839/224564757-728676b0-03de-494d-95ee-f48146e0e505.png">


## Задание 4

1. Сохраните ваш Dashboard.Для этого перейдите в настройки Dashboard, выберите в боковом меню «JSON MODEL». Далее скопируйте отображаемое json-содержимое в отдельный файл и сохраните его.
1. В качестве решения задания приведите листинг этого файла.

[Dashboard](https://github.com/t0hab/devops-19/blob/main/MNT-19/10-monitoring-03-grafana/dashboard.json)
