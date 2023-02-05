# Домашнее задание к занятию "10.Jenkins"

## Подготовка к выполнению

1. Создать 2 VM: для jenkins-master и jenkins-agent.
![image](https://user-images.githubusercontent.com/103331839/216823214-68bad32f-b516-458f-954b-0ab7bfcd3686.png)

2. Установить jenkins при помощи playbook'a.
![image](https://user-images.githubusercontent.com/103331839/216823230-cdd0fe80-8a44-49b0-a4aa-e1fd98657a66.png)


3. Запустить и проверить работоспособность.
![image](https://user-images.githubusercontent.com/103331839/216823366-8eee80b6-c57e-416b-9c86-1fce2530fda8.png)

4. Сделать первоначальную настройку.
![image](https://user-images.githubusercontent.com/103331839/216824114-5c72aa99-3ac3-4eb7-a145-fc10f136aa63.png)
![image](https://user-images.githubusercontent.com/103331839/216824382-8f0c2fc5-a50a-4b40-b2da-3e5d48c385ba.png)


## Основная часть

1. Сделать Freestyle Job, который будет запускать `molecule test` из любого вашего репозитория с ролью.
2. Сделать Declarative Pipeline Job, который будет запускать `molecule test` из любого вашего репозитория с ролью.
3. Перенести Declarative Pipeline в репозиторий в файл `Jenkinsfile`.
4. Создать Multibranch Pipeline на запуск `Jenkinsfile` из репозитория.
5. Создать Scripted Pipeline, наполнить его скриптом из [pipeline](./pipeline).
6. Внести необходимые изменения, чтобы Pipeline запускал `ansible-playbook` без флагов `--check --diff`, если не установлен параметр при запуске джобы (prod_run = True), по умолчанию параметр имеет значение False и запускает прогон с флагами `--check --diff`.
7. Проверить работоспособность, исправить ошибки, исправленный Pipeline вложить в репозиторий в файл `ScriptedJenkinsfile`.
8. Отправить ссылку на репозиторий с ролью и Declarative Pipeline и Scripted Pipeline.
