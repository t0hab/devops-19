# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

## Обязательные задания

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:
	```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
	```
  Нужно найти и исправить все ошибки, которые допускает наш сервис
  
### Ответ
```json
{ "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
В поле IP недостаточно ковычек.

Верный вариант
```json
{ "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip": "71.78.22.43"
            }
        ]
    }
```

2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
#!/usr/bin/env python3
import socket
import time
import datetime
import json
import yaml

timeout = 1
hosts = {'drive.google.com': '', 'mail.google.com': '', 'google.com': ''}

while True:
    for name, host in hosts.items():
        new_host = socket.gethostbyname(name)
        if new_host != host:
            print(str(datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")) + f'[ERROR] {name} | Выявленно несоответствие IP-адресов: Предыдущий адрес - {host} Новый адрес - {new_host}')
            hosts[name] = new_host
            with open("hosts.json", "w") as hosts_json:
                hosts_json.write(json.dumps(hosts, indent=2))
            with open("hosts.yaml", "w") as hosts_yaml:
                hosts_yaml.write(yaml.dump(hosts, explicit_start=True, explicit_end=True))
        else:
            time.sleep(timeout)
            print(f'{name} - {host}')
```

### Вывод скрипта при запуске при тестировании:
```bash
drive.google.com - 64.233.161.194
mail.google.com - 64.233.165.17
google.com - 64.233.164.139
drive.google.com - 64.233.161.194
20:51:43 07-08-2022[ERROR] mail.google.com | Выявленно несоответствие IP-адресов: Предыдущий адрес - 64.233.165.17 Новый адрес - 64.233.165.83
google.com - 64.233.164.139
drive.google.com - 64.233.161.194
20:51:45 07-08-2022[ERROR] mail.google.com | Выявленно несоответствие IP-адресов: Предыдущий адрес - 64.233.165.83 Новый адрес - 108.177.14.19
google.com - 64.233.164.139
drive.google.com - 64.233.161.194
mail.google.com - 108.177.14.19
google.com - 64.233.164.139
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
{
  "drive.google.com": "173.194.222.194",
  "mail.google.com": "108.177.14.19",
  "google.com": "64.233.164.139"
}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
---
drive.google.com: 173.194.222.194
google.com: 64.233.164.139
mail.google.com: 108.177.14.19
...
```
