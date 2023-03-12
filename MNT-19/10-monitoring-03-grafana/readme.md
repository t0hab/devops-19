# Домашнее задание к занятию 14 «Средство визуализации Grafana»

## Обязательные задания

### Задание 1

1. Используя директорию [help](./help) внутри этого домашнего задания, запустите связку prometheus-grafana.

<img width="1035" alt="image" src="https://user-images.githubusercontent.com/103331839/224560011-f5c9b45c-b336-47d9-8283-157995ba375b.png">

2. Зайдите в веб-интерфейс grafana, используя авторизационные данные, указанные в манифесте docker-compose.

<img width="1425" alt="image" src="https://user-images.githubusercontent.com/103331839/224560081-3671c031-db96-48b3-a41b-e8c979bd7b13.png">

3. Подключите поднятый вами prometheus, как источник данных.

<img width="1427" alt="image" src="https://user-images.githubusercontent.com/103331839/224562783-d956afad-0958-48f8-8025-bf55fa5a590d.png">

4. Решение домашнего задания — скриншот веб-интерфейса grafana со списком подключенных Datasource.

<img width="970" alt="image" src="https://user-images.githubusercontent.com/103331839/224562797-6a2f5263-bae2-422c-b0fd-1764dc29d1ab.png">


## Задание 2

Изучите самостоятельно ресурсы:

1. [PromQL tutorial for beginners and humans](https://valyala.medium.com/promql-tutorial-for-beginners-9ab455142085).
1. [Understanding Machine CPU usage](https://www.robustperception.io/understanding-machine-cpu-usage).
1. [Introduction to PromQL, the Prometheus query language](https://grafana.com/blog/2020/02/04/introduction-to-promql-the-prometheus-query-language/).

Создайте Dashboard и в ней создайте Panels:

- утилизация CPU для nodeexporter (в процентах, 100-idle);
- CPULA 1/5/15;
- количество свободной оперативной памяти;
- количество места на файловой системе.

Для решения этого задания приведите promql-запросы для выдачи этих метрик, а также скриншот получившейся Dashboard.

## Задание 3

1. Создайте для каждой Dashboard подходящее правило alert — можно обратиться к первой лекции в блоке «Мониторинг».
1. В качестве решения задания приведите скриншот вашей итоговой Dashboard.

## Задание 4

1. Сохраните ваш Dashboard.Для этого перейдите в настройки Dashboard, выберите в боковом меню «JSON MODEL». Далее скопируйте отображаемое json-содержимое в отдельный файл и сохраните его.
1. В качестве решения задания приведите листинг этого файла.

