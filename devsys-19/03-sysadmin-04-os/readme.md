# Домашнее задание к занятию "3.4. Операционные системы, лекция 2"

## Доработка

1. Предлагаю уточнить как именно в службу будут передаваться дополнительные опции. Замечу, что речь идёт не о переменных окружения, а об опциях (параметрах) запуска службы.

### Ответ:

Спасибо за мануал. Воспользовался информацией из freedesktop 


```bash
[Unit]
Description=Node Exporter
[Service]
ExecStart=/opt/node_exporter/node_exporter $MY_OPTION
EnvironmentFile=/etc/default/node_exporter 
 
[Install]
WantedBy=default.target
```

2. Задание 6
Вы запустили sleep без параметра и он закончился быстрее, чем был вызван nsenter. Попробуйте выполнить так, чтобы PID = 1
### Ответ:
Действительно, ранее sleep у меня не ставился в 1 час. Всё исправил, ниже вывод

```bash
root        1316  0.0  0.0   5476   596 pts/1    S+   21:49   0:00 sleep 1h
root        1317  0.0  0.3   8892  3440 pts/0    R+   21:50   0:00 ps aux
root@vagrant:~# nsenter -t 1316 -p -m
root@vagrant:/# ps
    PID TTY          TIME CMD
      2 pts/0    00:00:00 bash
     13 pts/0    00:00:00 ps
root@vagrant:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   5476   596 pts/1    S+   21:49   0:00 sleep 1h
root           2  0.0  0.4   7236  4112 pts/0    S    21:50   0:00 -bash
root          14  0.0  0.3   8892  3356 pts/0    R+   21:52   0:00 ps aux
root@vagrant:/# 
```



---
## Домашняя работа

1. На лекции мы познакомились с node_exporter. В демонстрации его исполняемый файл запускался в background. Этого достаточно для демо, но не для настоящей production-системы, где процессы должны находиться под внешним управлением. Используя знания из лекции по systemd, создайте самостоятельно простой unit-файл для node_exporter:

    * поместите его в автозагрузку,
    * предусмотрите возможность добавления опций к запускаемому процессу через внешний файл (посмотрите, например, на `systemctl cat cron`),
    * удостоверьтесь, что с помощью systemctl процесс корректно стартует, завершается, а после перезагрузки автоматически поднимается.


     ## Ответ
     Скачиваем нужный архив на свою машину [node_exporter](https://github.com/prometheus/node_exporter/releases) 
     
     Распаковываем `tar xvfz node_exporter-1.3.1.linux-386.tar.gz`
     
     Для удобства скопирую исполняемый файл в /usr/local/bin `sudo cp ~/Загрузки/node_exporter-1.3.1.linux-386/node_exporter /usr/local/bin` 
     
     Создам юнит файл systemd для его запуска `sudo systemctl edit --full --force node_exporter.service`
     ```
      [Unit]
      Description=Node Exporter
      Wants=network-online.target
      After=network-online.target
      [Service]
      User=node_exporter
      Group=node_exporter
      Type=simple
      ExecStart=/usr/local/bin/node_exporter
      [Install]
      WantedBy=multi-user.target
      ```
      
      Запускаем `sudo systemctl start node_exporter`
     
     Проверяем статус нашего сервиса `sudo systemctl status node_exporter`
     ![alt text](https://i.ibb.co/LNmTr8D/image.png)
     
     Подключаем для нашего сервиса автозапуск `sudo systemctl enable node_exporter`
     
     Дополнение: Необходимо проверить заранее не занят ли порт 9100, так как его использует node_exporter
     
     Скриншот работы Node Exporter с браузерной странички на нашем адрессе 
     ![alt text](https://i.ibb.co/4sD4trk/image.png)
    
2. Ознакомьтесь с опциями node_exporter и выводом /metrics по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.
      
      ## Ответ
      Перешел, для ознакомления с `metrics`, на http://localhost:9100/metrics
      
      * CPU `node_cpu_seconds_total{cpu="1",mode="system"} 7.31` `node_cpu_seconds_total{cpu="1",mode="user"} 14.8` `node_cpu_seconds_total{cpu="1",mode="idle"} 287.38`
      `node_cpu_seconds_total{cpu="0",mode="system"} 8.5` `node_cpu_seconds_total{cpu="0",mode="user"} 16.11` `node_cpu_seconds_total{cpu="0",mode="idle"} 277.67`
      
      * MEMORY `node_memory_MemAvailable_bytes 2.712117248e+09` `node_memory_MemFree_bytes 1.546317824e+09` `node_memory_MemTotal_bytes 4.1227264e+09`
      * DISK `node_disk_io_time_seconds_total{device="sda"} 152.728` `node_disk_read_bytes_total{device="sda"} 1.280625664e+09` `node_disk_read_time_seconds_total{device="sda"} 480.72` `node_disk_write_time_seconds_total{device="sda"} 446.18600000000004` 
      * NETWORK `node_network_receive_errs_total{device="enp0s3"} 0``node_network_receive_bytes_total{device="enp0s3"} 1.486831e+06` `node_network_transmit_bytes_total{device="enp0s3"} 130269` `node_network_transmit_errs_total{device="enp0s3"} 0`

3. Установите в свою виртуальную машину Netdata. Воспользуйтесь готовыми пакетами для установки (sudo apt install -y netdata). После успешной установки:
   * в конфигурационном файле `/etc/netdata/netdata.conf` в секции [web] замените значение с localhost на `bind to = 0.0.0.0`,
    * добавьте в Vagrantfile проброс порта Netdata на свой локальный компьютер и сделайте `vagrant reload`:

    ```bash
    config.vm.network "forwarded_port", guest: 19999, host: 19999
    ```

    После успешной перезагрузки в браузере *на своем ПК* (не в виртуальной машине) вы должны суметь зайти на `localhost:19999`. Ознакомьтесь с метриками, которые по умолчанию собираются Netdata и с комментариями, которые даны к этим метрикам.
    
     ## Ответ
     
     ![node_exporter](https://i.ibb.co/59Hgk17/image.png)

4. Можно ли по выводу dmesg понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?

     ## Ответ
      
     Да. Можно загрепать для удобного визуала
     ![node_exporter](https://i.ibb.co/PmHdQJb/image.png)

5. Как настроен sysctl fs.nr_open на системе по-умолчанию? Узнайте, что означает этот параметр. Какой другой существующий лимит не позволит достичь такого числа (ulimit --help)?

     ## Ответ
     
     Данный параметр означает максимальное кол-во открытых дискрипторов

     ```
     vagrant@vagrant:~$ sudo sysctl -a | grep fs.nr_open
     fs.nr_open = 1048576
     ```
     Другой существующий лимит через ulimit
     
     ```
      vagrant@vagrant:~$ ulimit -a
      core file size          (blocks, -c) 0
      data seg size           (kbytes, -d) unlimited
      scheduling priority             (-e) 0
      file size               (blocks, -f) unlimited
      pending signals                 (-i) 3707
      max locked memory       (kbytes, -l) 65536
      max memory size         (kbytes, -m) unlimited
      open files                      (-n) 1024
      pipe size            (512 bytes, -p) 8
      POSIX message queues     (bytes, -q) 819200
      real-time priority              (-r) 0
      stack size              (kbytes, -s) 8192
      cpu time               (seconds, -t) unlimited
      max user processes              (-u) 3707
      virtual memory          (kbytes, -v) unlimited
      file locks                      (-x) unlimited
      vagrant@vagrant:~$ ulimit -Sn
      1024
      vagrant@vagrant:~$ ulimit -Hn
      1048576
      ```
6. Запустите любой долгоживущий процесс (не ls, который отработает мгновенно, а, например, sleep 1h) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через nsenter. Для простоты работайте в данном задании под root (sudo -i). Под обычным пользователем требуются дополнительные опции (--map-root-user) и т.д.
     
     ## Ответ
     
     запустил sleep 1h 
     
     ![picture](https://i.ibb.co/wMPYCRz/image.png)
     
   ```
   root@vagrant:~# ps -e | grep sleep
   1908 pts/3    00:00:00 sleep
   root@vagrant:~# nsenter --target 1908 --pid --mount
   root@vagrant:/# ps
   PID TTY          TIME CMD
   1950 pts/1    00:00:00 sudo
   1951 pts/1    00:00:00 bash
   1983 pts/1    00:00:00 nsenter
   1984 pts/1    00:00:00 bash
   1995 pts/1    00:00:00 ps
   root@vagrant:/# 
   ```
7. Найдите информацию о том, что такое :(){ :|:& };:. Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (это важно, поведение в других ОС не проверялось). Некоторое время все будет "плохо", после чего (минуты) – ОС должна стабилизироваться. Вызов dmesg расскажет, какой механизм помог автоматической стабилизации. Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?

     ## Ответ

   dmesg выдал следующее 
   
   `[ 3419.705719] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-3.scope`
   
   число процессов можно поменять с помощью `ulimit -u ^кол-во^` 
   
   так мы указываем максимальное количество процессов, доступных одному пользователю

     