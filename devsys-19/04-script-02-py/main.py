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