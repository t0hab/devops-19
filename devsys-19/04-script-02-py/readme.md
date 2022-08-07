# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

1. Есть скрипт:
	```python
    #!/usr/bin/env python3
	a = 1
	b = '2'
	c = a + b
	```
	* Какое значение будет присвоено переменной c? В данном случае мы пытаемся объединить числовое значение со строкой, по итогу мы получим ошибку, а к `c` не будет присвоено значение.

	* Как получить для переменной `c` значение 12? 	`a = '1' b = '2' c = a+b`

	* Как получить для переменной `c` значение 3?	`a = 1 b = 2  c = a+b`


2. Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
    #!/usr/bin/env python3
    import os
	bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
	result_os = os.popen(' && '.join(bash_command)).read()
    is_change = False
	for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = result.replace('\tmodified:   ', '')
            print(prepare_result)
            break
```
## Ответ

Закомментил лишнее 
```python
#!/usr/bin/env python3
import os
bash_command = ["cd /Users/t0hab/Documents/Нетология/Обучение/HomeWork/04-script-02-py", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
# is_change = False
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено:   ', '')
        print(prepare_result)
        # break
```
	
3. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ответ
Тут нас выручит аргумент sys.argv
```python
#!/usr/bin/env python3
import os
import sys
path = sys.argv[1]
bash_command = ["cd "+path, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
# is_change = False
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено:   ', '')
        print("Файлы в которых внесены изменения: " +prepare_result)
        # break
```

Так же, для эстетики, создал скриптик input.py.
При его запуске он запрашивает путь к нашей директории, сопоставляет его с командами из bash и выводит ответ на экран

```bash
(venv) ┌─(~/Documents/Нетология/Обучение/HomeWork/04-script-02-py)───────────────────────────────────────────────────────────────────────────────(t0hab@MacBook-Air-Tokhir:s000)─┐
└─(22:06:52 on main ✭)──> python input.py                                                                                                                   ──(Sun,Jul31)─┘
Введите путь к вашему репозиторию: ~/Documents/Нетология/Обучение/HomeWork/04-script-02-py
Ищем изменённые файлы в репозитории ~/Documents/Нетология/Обучение/HomeWork/04-script-02-py
Файлы в которых внесены изменения
   unknown_file
(venv) ┌─(~/Documents/Нетология/Обучение/HomeWork/04-script-02-py)───────────────────────────────────────────────────────────────────────────────(t0hab@MacBook-Air-Tokhir:s000)─┐
└─(22:07:20 on main ✹ ✭)──>   
```

![image1](https://github.com/t0hab/04-script-02-py/blob/main/Image1/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-07-31%20%D0%B2%2021.53.27.png)


4. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.

### Ответ

Скрипт
```python
#!/usr/bin/env python3
import socket
import time
import datetime
N = 1
timeout = 3
hosts = {'drive.google.com':'173.194.222.194', 'mail.google.com':'142.251.1.83', 'google.com':'142.251.1.139'}
init=0
while 1==1:
  for host in hosts:
    ip = socket.gethostbyname(host)
    if ip != hosts[host]:
      if N==1 and init !=1:
        print(str(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")) + '[ERROR]' + str(host) +' Предыдущий адрес: '+hosts[host]+' Новый адрес: '+ip)
      hosts[host]=ip
  N+=1
  if N >= 10:
    break
  time.sleep(timeout)
```
Вывод скрипта
```bash
PS E:\netology\GIT_REP\04-script-02-py> python .\host.py
08:58:58 02-08-2022[ERROR]mail.google.com Предыдущий адрес: 142.251.1.83 Новый адрес: 64.233.165.18
08:58:58 02-08-2022[ERROR]google.com Предыдущий адрес: 142.251.1.139 Новый адрес: 74.125.131.138
PS E:\netology\GIT_REP\04-script-02-py> 
```