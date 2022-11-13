```bash
# пинг на localhost
ansible -m ping localhost

# пинг на всех хостах из inventory
ansible -m ping -i inventory.yml all

# пинг на всех хостах группы <group_name>
ansible -m ping -i inventory.yml <group_name>

# запуск site на хостах из test
ansible-playbook site.yml -i inventory/test.yml

# показать хосты группы 
ansible-inventory -i inventory.yml --graph <group_name>

# показать все переменные всех хостов из inventory 
ansible-inventory -i inventory.yml --list 

# показать все переменные хоста из inventory 
ansible-inventory -i inventory.yml --list <hostname> 

# показать документацию по плагину 
ansible-doc <plugin_name>

# создать новый зашифрованный файл 
ansible-vault create <file_name>

# отредактировать зашифрованный файл 
ansible-vault edit <file_name>

# посмотреть зашифрованный файл 
ansible-vault view <file_name>

# поменять пароль у файла 
ansible-vault rekey <file_name>

# расшифровать файл 
ansible-vault decrypt <file_name>

```