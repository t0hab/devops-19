#!/usr/bin/env python3
import os
code = 'python main.py '
path = input('Введите путь к вашему репозиторию: ')
print('Ищем изменённые файлы в репозитории '+path)
os.system(code +path)

# через subproccess не получилось выполнить
# import subprocess
# subprocess.run(["python main.py " +path])