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