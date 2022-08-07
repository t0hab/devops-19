# Доработка
Задание 1, 2
Какие коды ответов получены? Что они обозначают?

### Ответ:
По первому заданию ответный код получил 301 `HTTP/1.1 301 Moved Permanently` - означает что запрошенный адрес перемещен навсегда
По второму заданию получил ответный код 200 - означает успешное выполнение, то есть то что мы запросили - получили.

---

# Домашнее задание к занятию "3.6. Компьютерные сети, лекция 1"

1. Работа c HTTP через телнет.
- Подключитесь утилитой телнет к сайту stackoverflow.com
`telnet stackoverflow.com 80`
- отправьте HTTP запрос
```bash
GET /questions HTTP/1.0
HOST: stackoverflow.com
[press enter]
[press enter]
```
- В ответе укажите полученный HTTP код, что он означает?

### Ответ:
```bash
vagrant@vagrant:~$ telnet stackoverflow.com 80
Trying 151.101.193.69...
Connected to stackoverflow.com.
Escape character is '^]'.
GET /questions HTTP/1.0
HOST: stackoverflow.com
HTTP/1.1 301 Moved Permanently
cache-control: no-cache, no-store, must-revalidate
location: https://stackoverflow.com/questions
x-request-guid: d3e397f1-ab59-4b12-8a9b-aaac2d42f5a4
feature-policy: microphone 'none'; speaker 'none'
content-security-policy: upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com
Accept-Ranges: bytes
Date: Sat, 02 Jul 2022 18:59:54 GMT
Via: 1.1 varnish
Connection: close
X-Served-By: cache-ams21067-AMS
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1656788395.825638,VS0,VE76
Vary: Fastly-SSL
X-DNS-Prefetch-Control: off
Set-Cookie: prov=6fa50547-ce9b-cd9d-89ca-79c4ba15f53c; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly
Connection closed by foreign host.
vagrant@vagrant:~$ 
```
---

2. Повторите задание 1 в браузере, используя консоль разработчика F12.
- откройте вкладку `Network`
- отправьте запрос http://stackoverflow.com
- найдите первый ответ HTTP сервера, откройте вкладку `Headers`
- укажите в ответе полученный HTTP код.
- проверьте время загрузки страницы, какой запрос обрабатывался дольше всего?
- приложите скриншот консоли браузера в ответ.

### Ответ:

Скорость загрузки страницы составила 332 ms
  
Самый долгий запрос представлен на скриншоте
  
  
![image](https://i.ibb.co/BrsYxMf/image.png)  
  
![image](https://i.ibb.co/MChzCcP/image.png)

---
3. Какой IP адрес у вас в интернете?
### Ответ:

Не хотел показывать свой ip в открытом доступе, поэтому включил vpn
![image](https://i.ibb.co/p0dG4K9/image.png)

---
4. Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой `whois`
### Ответ:

* Провайдер - Scaleway Dedibox
* Автономная система - AS12876

```bash
vagrant@vagrant:~$ whois 62.210.127.130 
% This is the RIPE Database query service.
% The objects are in RPSL format.
%
% The RIPE Database is subject to Terms and Conditions.
% See http://www.ripe.net/db/support/db-terms-conditions.pdf
% Note: this output has been filtered.
%       To receive output for a database update, use the "-B" flag.
% Information related to '62.210.0.0 - 62.210.127.255'
% Abuse contact for '62.210.0.0 - 62.210.127.255' is 'abuse@online.net'
inetnum:        62.210.0.0 - 62.210.127.255
org:            ORG-ONLI1-RIPE
netname:        SCALEWAY-DEDIBOX
descr:          Scaleway Dedibox
remarks:        Abuse reports : https://abuse.online.net/
country:        FR
admin-c:        IENT-RIPE
tech-c:         IENT-RIPE
status:         LIR-PARTITIONED PA
mnt-by:         MNT-TISCALIFR-B2B
mnt-by:         ONLINE-NET-MNT
created:        2012-11-02T11:39:45Z
last-modified:  2022-05-05T15:40:34Z
source:         RIPE
organisation:   ORG-ONLI1-RIPE
mnt-ref:        MNT-TISCALIFR-B2B
org-name:       Scaleway
org-type:       OTHER
address:        8 rue de la ville l'eveque 75008 PARIS
abuse-c:        AR32851-RIPE
mnt-ref:        ONLINE-NET-MNT
mnt-by:         ONLINE-NET-MNT
created:        2015-07-10T15:20:41Z
last-modified:  2022-05-03T15:39:01Z
source:         RIPE # Filtered
role:           SCALEWAY
remarks:        known as Online S.A.S. / Iliad-Entreprises
address:        8 rue de la ville l'évêque
address:        75008 Paris
address:        France
abuse-mailbox:  abuse@online.net
tech-c:         TTFR1-RIPE
nic-hdl:        IENT-RIPE
mnt-by:         ONLINE-NET-MNT
created:        2012-10-25T13:21:59Z
last-modified:  2022-05-03T15:50:16Z
source:         RIPE # Filtered
% Information related to '62.210.0.0/16AS12876'
route:          62.210.0.0/16
descr:          Scaleway
descr:          Paris, France
mnt-lower:      ONLINE-NET-MNT
origin:         AS12876
mnt-by:         MNT-TISCALIFR
mnt-lower:      ONLINE-NET-MNT
created:        2013-08-02T09:07:46Z
last-modified:  2022-05-03T10:05:58Z
source:         RIPE
% This query was served by the RIPE Database Query Service version 1.103 (HEREFORD)
vagrant@vagrant:~$ 
```
---
5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой `traceroute`
### Ответ:

```bash
vagrant@vagrant:~$ traceroute -An 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  10.0.2.2 [*]  0.154 ms  0.112 ms  0.095 ms
 2  192.168.0.1 [*]  3.022 ms  3.577 ms  3.526 ms
 3  10.0.0.1 [*]  3.505 ms  3.390 ms  3.326 ms
 4  172.28.131.5 [*]  3.828 ms  3.795 ms  3.655 ms
 5  * * *
 6  195.208.208.232 [AS5480]  12.041 ms  10.861 ms  11.652 ms
 7  108.170.250.99 [AS15169]  12.703 ms * *
 8  72.14.234.54 [AS15169]  30.497 ms 142.251.238.82 [AS15169]  29.283 ms 142.250.239.64 [AS15169]  29.211 ms
 9  72.14.232.86 [AS15169]  35.386 ms 142.251.238.66 [AS15169]  29.074 ms 172.253.65.159 [AS15169]  28.282 ms
10  216.239.42.23 [AS15169]  26.886 ms 209.85.246.111 [AS15169]  26.816 ms 172.253.51.245 [AS15169]  33.055 ms
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * 8.8.8.8 [AS15169]  34.093 ms *
```
---
6. Повторите задание 5 в утилите `mtr`. На каком участке наибольшая задержка - delay?
### Ответ:

Наибольшая задержка на строке №6, хотя сильная потеря пакетов у нас идет на №5

![image](https://i.ibb.co/mNf2zXd/image.png)

---

7. Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой `dig`
### Ответ:

Какие DNS сервера отвечают за доменное имя dns.google 
```bash
vagrant@vagrant:~$ dig NS  dns.google
; <<>> DiG 9.16.1-Ubuntu <<>> NS dns.google
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54470
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;dns.google.			IN	NS
;; ANSWER SECTION:
dns.google.		6812	IN	NS	ns2.zdns.google.
dns.google.		6812	IN	NS	ns4.zdns.google.
dns.google.		6812	IN	NS	ns1.zdns.google.
dns.google.		6812	IN	NS	ns3.zdns.google.
;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Sat Jul 02 20:52:13 UTC 2022
;; MSG SIZE  rcvd: 116
vagrant@vagrant:~$ 
```
Какие A записи
```bash
vagrant@vagrant:~$ dig A dns.google
; <<>> DiG 9.16.1-Ubuntu <<>> A dns.google
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56065
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;dns.google.			IN	A
;; ANSWER SECTION:
dns.google.		566	IN	A	8.8.4.4
dns.google.		566	IN	A	8.8.8.8
;; Query time: 4 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Sat Jul 02 20:53:34 UTC 2022
;; MSG SIZE  rcvd: 71
vagrant@vagrant:~$ 
```
8. Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой `dig`
### Ответ:
```bash
vagrant@vagrant:~$ dig -x 8.8.8.8
; <<>> DiG 9.16.1-Ubuntu <<>> -x 8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 23804
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;8.8.8.8.in-addr.arpa.		IN	PTR
;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.	3668	IN	PTR	dns.google.
;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Sat Jul 02 20:56:33 UTC 2022
;; MSG SIZE  rcvd: 73
vagrant@vagrant:~$ dig -x 8.8.4.4
; <<>> DiG 9.16.1-Ubuntu <<>> -x 8.8.4.4
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 50899
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;4.4.8.8.in-addr.arpa.		IN	PTR
;; ANSWER SECTION:
4.4.8.8.in-addr.arpa.	8020	IN	PTR	dns.google.
;; Query time: 3 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Sat Jul 02 20:56:40 UTC 2022
;; MSG SIZE  rcvd: 73
vagrant@vagrant:~$ 
```