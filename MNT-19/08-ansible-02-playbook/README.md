# Домашнее задание к занятию "2. Работа с Playbook"

## Подготовка к выполнению

1. (Необязательно) Изучите, что такое [clickhouse](https://www.youtube.com/watch?v=fjTNS2zkeBs) и [vector](https://www.youtube.com/watch?v=CgEhyffisLY)
2. Создайте свой собственный (или используйте старый) публичный репозиторий на github с произвольным именем.
3. Скачайте [playbook](./playbook/) из репозитория с домашним заданием и перенесите его в свой репозиторий.
4. Подготовьте хосты в соответствии с группами из предподготовленного playbook.

## Основная часть

1. Приготовьте свой собственный inventory файл `prod.yml`.

Пытался пробиться через docker, но выходила ошибка tmp, будто не хватает ему прав достучаться.
Поднял машину (centos7) удаленно на стационарном ПК и решил к нему пробросить сеть.
Далее столкнулся с проблемой подключения по IP, в гугле нашел способ подключения по ssh через `ansible_ssh_host`
```yml
---
clickhouse:
  hosts:
    clickhouse-01:
      ansible_ssh_host: 192.168.0.252
      ansible_ssh_user: root
      #ansible_connection: 192.168.0.252
      #ansible_user: t0hab
vector:
  hosts:
    vector-01:
      ansible_ssh_host: 192.168.0.252
      ansible_ssh_user: root
      #ansible_connection: 192.168.0.252
      #ansible_user: t0hab

#clickhouse ansible_host=192.168.0.252 ansible_user=t0hab ansible_become=true
#vector ansible_host=192.168.0.252 ansible_user=t0hab ansible_become=true
```
2. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает [vector](https://vector.dev).

```yaml
---
- name: Install Clickhouse
  hosts: clickhouse
  tasks:
    - block:
        - name: Get clickhouse distrib
          ansible.builtin.get_url:
            url: "https://packages.clickhouse.com/rpm/stable/{{ item }}-{{ clickhouse_version }}.noarch.rpm"
            dest: "./{{ item }}-{{ clickhouse_version }}.rpm"
          with_items: "{{ clickhouse_packages }}"
      rescue:
        - name: Get clickhouse distrib
          ansible.builtin.get_url:
            url: "https://packages.clickhouse.com/rpm/stable/clickhouse-common-static-{{ clickhouse_version }}.x86_64.rpm"
            dest: "./clickhouse-common-static-{{ clickhouse_version }}.rpm"
    - name: Install clickhouse packages
      become: true
      ansible.builtin.yum:
        name:
          - clickhouse-common-static-{{ clickhouse_version }}.rpm
          - clickhouse-client-{{ clickhouse_version }}.rpm
          - clickhouse-server-{{ clickhouse_version }}.rpm
    - name: Start clickhouse service
      become: true
      ansible.builtin.service:
        name: clickhouse-server
        state: restarted
    - name: Verify clickhouse-server is listening on 9000
      wait_for:
        port: 9000
        delay: 5
        timeout: 300
    - name: Create database
      command: clickhouse-client -q 'create database logs;'
      register: create_db
      failed_when: create_db.rc | default('') != 0 and create_db.rc | default('') !=82
      changed_when: create_db.rc | default('') == 0
- name: Install Vector
  hosts: vector
  handlers:
    - name: Start vector service
      become: true
      ansible.builtin.service:
        name: vector
        state: restarted
  tasks:
    - name: Get vector distrib
      ansible.builtin.get_url:
        url: "https://packages.timber.io/vector/{{ vector_version }}/vector-{{ vector_version }}-1.x86_64.rpm"
        dest: "./vector-{{ vector_version }}-1.x86_64.rpm"
    - name: Install vector package
      become: true
      ansible.builtin.yum:
        name:
          - vector-{{ vector_version }}-1.x86_64.rpm
      notify: Start vector service
```

3. При создании tasks рекомендую использовать модули: `get_url`, `template`, `unarchive`, `file`.

`выполнил`

4. Tasks должны: скачать нужной версии дистрибутив, выполнить распаковку в выбранную директорию, установить vector.

`выполнил`

5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.

Нужно время чтобы еще разобраться с Ansible и понять как исправить ошибки.
Обязательно этим займусь.

```yaml
                              Rule Violation Summary                              
 count tag                    profile    rule associated tags                     
     1 jinja[spacing]         basic      formatting (warning)                     
     1 name[missing]          basic      idiom                                    
     3 risky-file-permissions safety     unpredictability, experimental (warning) 
     2 fqcn[action-core]      production formatting                               

Failed after min profile: 3 failure(s), 4 warning(s) on 1 files.
```

6. Попробуйте запустить playbook на этом окружении с флагом `--check`.

```yaml
❯ ansible-playbook -i inventory/prod.yml site.yml --check --ask-pass
SSH password: 

PLAY [Install Clickhouse] **************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Get clickhouse distrib] **********************************************************************************************************************************************
ok: [clickhouse-01] => (item=clickhouse-client)
ok: [clickhouse-01] => (item=clickhouse-server)
failed: [clickhouse-01] (item=clickhouse-common-static) => {"ansible_loop_var": "item", "changed": false, "dest": "./clickhouse-common-static-21.10.6.2-2.rpm", "elapsed": 0, "gid": 0, "group": "root", "item": "clickhouse-common-static", "mode": "0644", "msg": "Request failed", "owner": "root", "response": "HTTP Error 404: Not Found", "secontext": "unconfined_u:object_r:admin_home_t:s0", "size": 189027626, "state": "file", "status_code": 404, "uid": 0, "url": "https://packages.clickhouse.com/rpm/stable/clickhouse-common-static-21.10.6.2-2.noarch.rpm"}

TASK [Get clickhouse distrib] **********************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install clickhouse packages] *****************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Start clickhouse service] ********************************************************************************************************************************************
changed: [clickhouse-01]

TASK [Verify clickhouse-server is listening on 9000] ***********************************************************************************************************************
skipping: [clickhouse-01]

TASK [Create database] *****************************************************************************************************************************************************
skipping: [clickhouse-01]

PLAY [Install Vector] ******************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [vector-01]

TASK [Get vector distrib] **************************************************************************************************************************************************
ok: [vector-01]

TASK [Install vector package] **********************************************************************************************************************************************
ok: [vector-01]

PLAY RECAP *****************************************************************************************************************************************************************
clickhouse-01              : ok=4    changed=1    unreachable=0    failed=0    skipped=2    rescued=1    ignored=0   
vector-01                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.

```yaml
❯ ansible-playbook -i inventory/prod.yml site.yml --diff --ask-pass
SSH password: 

PLAY [Install Clickhouse] **************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Get clickhouse distrib] **********************************************************************************************************************************************
ok: [clickhouse-01] => (item=clickhouse-client)
ok: [clickhouse-01] => (item=clickhouse-server)
failed: [clickhouse-01] (item=clickhouse-common-static) => {"ansible_loop_var": "item", "changed": false, "dest": "./clickhouse-common-static-21.10.6.2-2.rpm", "elapsed": 0, "gid": 0, "group": "root", "item": "clickhouse-common-static", "mode": "0644", "msg": "Request failed", "owner": "root", "response": "HTTP Error 404: Not Found", "secontext": "unconfined_u:object_r:admin_home_t:s0", "size": 189027626, "state": "file", "status_code": 404, "uid": 0, "url": "https://packages.clickhouse.com/rpm/stable/clickhouse-common-static-21.10.6.2-2.noarch.rpm"}

TASK [Get clickhouse distrib] **********************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install clickhouse packages] *****************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Start clickhouse service] ********************************************************************************************************************************************
changed: [clickhouse-01]

TASK [Verify clickhouse-server is listening on 9000] ***********************************************************************************************************************
ok: [clickhouse-01]

TASK [Create database] *****************************************************************************************************************************************************
ok: [clickhouse-01]

PLAY [Install Vector] ******************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [vector-01]

TASK [Get vector distrib] **************************************************************************************************************************************************
changed: [vector-01]

TASK [Install vector package] **********************************************************************************************************************************************
changed: [vector-01]

RUNNING HANDLER [Start vector service] *************************************************************************************************************************************
changed: [vector-01]

PLAY RECAP *****************************************************************************************************************************************************************
clickhouse-01              : ok=6    changed=1    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0   
vector-01                  : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.

```yaml
❯ ansible-playbook -i inventory/prod.yml site.yml --diff --ask-pass
SSH password: book -i inventory/prod.yml site.yml --diff --ask-pass

PLAY [Install Clickhouse] **************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Get clickhouse distrib] **********************************************************************************************************************************************
ok: [clickhouse-01] => (item=clickhouse-client)
ok: [clickhouse-01] => (item=clickhouse-server)
failed: [clickhouse-01] (item=clickhouse-common-static) => {"ansible_loop_var": "item", "changed": false, "dest": "./clickhouse-common-static-21.10.6.2-2.rpm", "elapsed": 0, "gid": 0, "group": "root", "item": "clickhouse-common-static", "mode": "0644", "msg": "Request failed", "owner": "root", "response": "HTTP Error 404: Not Found", "secontext": "unconfined_u:object_r:admin_home_t:s0", "size": 189027626, "state": "file", "status_code": 404, "uid": 0, "url": "https://packages.clickhouse.com/rpm/stable/clickhouse-common-static-21.10.6.2-2.noarch.rpm"}

TASK [Get clickhouse distrib] **********************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Install clickhouse packages] *****************************************************************************************************************************************
ok: [clickhouse-01]

TASK [Start clickhouse service] ********************************************************************************************************************************************
changed: [clickhouse-01]

TASK [Verify clickhouse-server is listening on 9000] ***********************************************************************************************************************
ok: [clickhouse-01]

TASK [Create database] *****************************************************************************************************************************************************
ok: [clickhouse-01]

PLAY [Install Vector] ******************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [vector-01]

TASK [Get vector distrib] **************************************************************************************************************************************************
ok: [vector-01]

TASK [Install vector package] **********************************************************************************************************************************************
ok: [vector-01]

PLAY RECAP *****************************************************************************************************************************************************************
clickhouse-01              : ok=6    changed=1    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0   
vector-01                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

9. Подготовьте README.md файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.

Playbook устанавливает пакеты clickhouse и vector на 2 хоста описаные в файле inventory\prod.yml
Также в playbook есть задача, которая проверяет каждые 5 секунд начал сервис clickhouse слушать 9000 порт или нет, таймаут 300 секунд.

10. Готовый playbook выложите в свой репозиторий, поставьте тег `08-ansible-02-playbook` на фиксирующий коммит, в ответ предоставьте ссылку на него.

[08-ansible-02-playbook](https://github.com/t0hab/devops-19/tree/main/MNT-19/08-ansible-02-playbook/playbook)
