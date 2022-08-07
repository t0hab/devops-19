# Домашнее задание к занятию "3.9. Элементы безопасности информационных систем"

# 1. Установите Bitwarden плагин для браузера. Зарегестрируйтесь и сохраните несколько паролей.
### Ответ
![img1](https://github.com/t0hab/03-sysadmin-09-security/blob/main/image/1.png)

---
# 2. Установите Google authenticator на мобильный телефон. Настройте вход в Bitwarden акаунт через Google authenticator OTP.
### Ответ
Решил использовать уже имеющийся аутентификатор от майкрософт. 
![img2](https://github.com/t0hab/03-sysadmin-09-security/blob/main/image/2.png)

![img3](https://github.com/t0hab/03-sysadmin-09-security/blob/main/image/3.png)
---
# 3. Установите apache2, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по HTTPS.
### Ответ
![img4](https://github.com/t0hab/03-sysadmin-09-security/blob/main/image/4.png)

![img5](https://github.com/t0hab/03-sysadmin-09-security/blob/main/image/5.png)

---
# 4. Проверьте на TLS уязвимости произвольный сайт в интернете (кроме сайтов МВД, ФСБ, МинОбр, НацБанк, РосКосмос, РосАтом, РосНАНО и любых госкомпаний, объектов КИИ, ВПК ... и тому подобное).
### Ответ
```bash
 Using "OpenSSL 1.0.2-chacha (1.0.2k-dev)" [~183 ciphers]
 on t0hab-pc:./bin/openssl.Linux.x86_64
 (built: "Jan 18 17:12:17 2019", platform: "linux-x86_64")
 Start 2022-07-18 09:10:18        -->> 188.114.98.171:443 (netology.ru) <<--
 Further IP addresses:   2a06:98c1:3123:a000:: 
 rDNS (188.114.98.171):  --
 Service detected:       HTTP
 Testing vulnerabilities 
 Heartbleed (CVE-2014-0160)                not vulnerable (OK), no heartbeat extension
 CCS (CVE-2014-0224)                       not vulnerable (OK)
 Ticketbleed (CVE-2016-9244), experiment.  not vulnerable (OK)
 ROBOT                                     not vulnerable (OK)
 Secure Renegotiation (RFC 5746)           supported (OK)
 Secure Client-Initiated Renegotiation     not vulnerable (OK)
 CRIME, TLS (CVE-2012-4929)                not vulnerable (OK)
 BREACH (CVE-2013-3587)                    potentially NOT ok, "gzip" HTTP compression detected. - only supplied "/" tested
                                           Can be ignored for static pages or if no secrets in the page
 POODLE, SSL (CVE-2014-3566)               not vulnerable (OK)
 TLS_FALLBACK_SCSV (RFC 7507)              Downgrade attack prevention supported (OK)
 SWEET32 (CVE-2016-2183, CVE-2016-6329)    VULNERABLE, uses 64 bit block ciphers
 FREAK (CVE-2015-0204)                     not vulnerable (OK)
 DROWN (CVE-2016-0800, CVE-2016-0703)      not vulnerable on this host and port (OK)
                                           make sure you don't use this certificate elsewhere with SSLv2 enabled services, see
                                           https://search.censys.io/search?resource=hosts&virtual_hosts=INCLUDE&q=A3C7D9A8D3805171D99EA61F5C80B8ADF49B93BA21EBB492D78512BA254E90A5
 LOGJAM (CVE-2015-4000), experimental      not vulnerable (OK): no DH EXPORT ciphers, no DH key detected with <= TLS 1.2
 BEAST (CVE-2011-3389)                     TLS1: ECDHE-RSA-AES128-SHA AES128-SHA ECDHE-RSA-AES256-SHA AES256-SHA DES-CBC3-SHA 
                                           VULNERABLE -- but also supports higher protocols  TLSv1.1 TLSv1.2 (likely mitigated)
 LUCKY13 (CVE-2013-0169), experimental     potentially VULNERABLE, uses cipher block chaining (CBC) ciphers with TLS. Check patches
 Winshock (CVE-2014-6321), experimental    not vulnerable (OK)
 RC4 (CVE-2013-2566, CVE-2015-2808)        no RC4 ciphers detected (OK)
 Done 2022-07-18 09:10:55 [  39s] -->> 188.114.98.171:443 (netology.ru) <<--
```
---
# 5. Установите на Ubuntu ssh сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.
 ### Ответ
 `openssh-server is already the newest version (1:8.2p1-4ubuntu0.5)`
 
 ```bash
 The key fingerprint is:
SHA256:XY2qlIdC3oePUAb9C/BXUGuJYrGmbCQFGXKJCa5liTM vagrant@vagrant
The key's randomart image is:
+---[RSA 3072]----+
|...o+=o.. .o.    |
|..o+o....o ..=   |
|E.+ . ooB...* .  |
|.=   * Bo*o+     |
|.     B So=.     |
|     . + *.      |
|        o .      |
|                 |
|                 |
+----[SHA256]-----+
```
 ```bash
vagrant@vagrant:~$ ssh-copy-id t0hab@192.168.0.217
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/vagrant/.ssh/id_rsa.pub"
The authenticity of host '192.168.0.217 (192.168.0.217)' can't be established.
ECDSA key fingerprint is SHA256:SE8D1rl0ocuW8je/cnBwiJtwkQudYdN0pkaxEfb/SGE.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
t0hab@192.168.0.217's password:
Number of key(s) added: 1
Now try logging into the machine, with:   "ssh 't0hab@192.168.0.217'"
and check to make sure that only the key(s) you wanted were added.
vagrant@vagrant:~$ ssh t0hab@192.168.0.217
Last login: Thu Jun 16 12:11:46 2022 from 192.168.0.217
┌─(~)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(10:34:10)──> whoiam                                                                                                                                                      ──(Вт,июл19)─┘
zsh: command not found: whoiam
┌─(~)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(10:34:53)──> whoami                                                                                                                                                127 ↵ ──(Вт,июл19)─┘
t0hab
┌─(~)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(10:34:59)──>   
```
 ---
# 6. Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH клиента, так чтобы вход на удаленный сервер осуществлялся по имени сервера.
### Ответ
```bash
vagrant@vagrant:~/.ssh$ ssh t0hab-pc
Last login: Tue Jul 19 10:58:44 2022 from 192.168.0.251
┌─(~)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(10:59:13)──> whoami                                                                                                                                                      ──(Вт,июл19)─┘
t0hab
┌─(~)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(10:59:41)──> pwd                                                                                                                                                         ──(Вт,июл19)─┘
/home/t0hab
┌─(~)─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────(t0hab@t0hab-pc:pts/1)─┐
└─(10:59:42)──>  
```
---
# 7. Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.
### Ответ
```bash
tcpdump: listening on enp0s3, link-type EN10MB (Ethernet), capture size 262144 bytes
100 packets captured
105 packets received by filter
0 packets dropped by kernel
```
![img](https://github.com/t0hab/03-sysadmin-09-security/blob/main/image/6.png)