# Домашнее задание к занятию "5. Оркестрация кластером Docker контейнеров на примере Docker Swarm"

## Задача 1

Дайте письменые ответы на следующие вопросы:

- В чём отличие режимов работы сервисов в Docker Swarm кластере: replication и global?
- Какой алгоритм выбора лидера используется в Docker Swarm кластере?
- Что такое Overlay Network?

## Ответ
- replication - мы указываем сколько идентичных задач хотим запустить. Например, мы решили развернуть сервис HTTP с тремя репликами, каждая из которых обслуживает один и то же контент.
  global - это сервис, который запускает одну задачу на каждой ноде. 
- Raft Consensus Algorithm. В случае неполучения heartbeat сообщения от текущего лидера фолловеры выжидают 150-300ms (election timeout). Если в указанный промежуток времени фолловер не получает приглашение проголосовать за какого-либо кандидата, то он сам объявляет себя кандидатом и рассылает такое приглашение. В случае получения большинства голосов кандидат объявляет себя лидером и периодически рассылает heartbeat сообщения остальным членам.
- Overlay Network - распределённая виртуальная сеть между хостами с docker'ом. Живёт поверх реальных сетей, подключенных к конкретным докер-нодам. Служит для прозрачного и безопасного обмена данными и управляющими командами между докер-контейнерами кластера. Маршрутизация данных автоматическая (конечному пользователю с ней заморачиваться не нужно).

## Задача 2

Создать ваш первый Docker Swarm кластер в Яндекс.Облаке

Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:
```
docker node ls
```
## Ответ
```bash
[root@node01 ~]# docker node ls
ID                            HOSTNAME             STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
wfldddpmizfsc2iefzh1zdknw *   node01.netology.yc   Ready     Active         Leader           20.10.19
sczh841jlr0o5ialv6wzls4ou     node02.netology.yc   Ready     Active         Reachable        20.10.19
zmalk1qd0j83mm7tsv5lkl8tl     node03.netology.yc   Ready     Active         Reachable        20.10.19
cp8pxtkhemehj3tb9tb184hu6     node04.netology.yc   Ready     Active                          20.10.19
jvet7b4nafftp90ez838wwlen     node05.netology.yc   Ready     Active                          20.10.19
ai6pnm6331zonvx9dchvl6lnn     node06.netology.yc   Ready     Active                          20.10.19
```

## Задача 3

Создать ваш первый, готовый к боевой эксплуатации кластер мониторинга, состоящий из стека микросервисов.

Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:
```
docker service ls
```
## Ответ
```bash
[root@node01 ~]# docker service ls
ID             NAME                                MODE         REPLICAS   IMAGE                                          PORTS
i9mdijmamckt   swarm_monitoring_alertmanager       replicated   1/1        stefanprodan/swarmprom-alertmanager:v0.14.0    
p3wg7r7ij47u   swarm_monitoring_caddy              replicated   1/1        stefanprodan/caddy:latest                      *:3000->3000/tcp, *:9090->9090/tcp, *:9093-9094->9093-9094/tcp
ma0vjgj8dmzl   swarm_monitoring_cadvisor           global       6/6        google/cadvisor:latest                         
l9wuwc1vwsoh   swarm_monitoring_dockerd-exporter   global       6/6        stefanprodan/caddy:latest                      
q2gjjqh3zkrk   swarm_monitoring_grafana            replicated   1/1        stefanprodan/swarmprom-grafana:5.3.4           
nz772m4qxivi   swarm_monitoring_node-exporter      global       6/6        stefanprodan/swarmprom-node-exporter:v0.16.0   
runuov48quxw   swarm_monitoring_prometheus         replicated   1/1        stefanprodan/swarmprom-prometheus:v2.5.0       
yss17c53st7w   swarm_monitoring_unsee              replicated   1/1        cloudflare/unsee:v0.8.0                        
[root@node01 ~]# 
```
