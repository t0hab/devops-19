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