# Домашнее задание к занятию "9.Процессы CI/CD"

## Подготовка к выполнению

1. Создаём 2 VM в yandex cloud со следующими параметрами: 2CPU 4RAM Centos7(остальное по минимальным требованиям)
2. Прописываем в [inventory](./infrastructure/inventory/cicd/hosts.yml) [playbook'a](./infrastructure/site.yml) созданные хосты
3. Добавляем в [files](./infrastructure/files/) файл со своим публичным ключом (id_rsa.pub). Если ключ называется иначе - найдите таску в плейбуке, которая использует id_rsa.pub имя и исправьте на своё
4. Запускаем playbook, ожидаем успешного завершения
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215356152-da343491-ee11-45e9-adf8-73c5952bab44.png">

5. Проверяем готовность Sonarqube через [браузер](http://localhost:9000)
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215356135-ecc2ab07-f57d-4e0a-b256-2a1b99e299c9.png">

6. Заходим под admin\admin, меняем пароль на свой
7.  Проверяем готовность Nexus через [бразуер](http://localhost:8081)
8. Подключаемся под admin\admin123, меняем пароль, сохраняем анонимный доступ
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215356141-9cf09fb3-3b8b-48d2-ae41-2c749b42e4d5.png">


## Знакомоство с SonarQube

### Основная часть

1. Создаём новый проект, название произвольное
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215356260-16efec15-d584-4027-b0a8-09145d696f2d.png">

3. Скачиваем пакет sonar-scanner, который нам предлагает скачать сам sonarqube
4. Делаем так, чтобы binary был доступен через вызов в shell (или меняем переменную PATH или любой другой удобный вам способ)
6. Проверяем `sonar-scanner --version`
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215356700-07776ff5-a4be-4f49-9955-f10657a73a68.png">

8. Запускаем анализатор против кода из директории [example](./example) с дополнительным ключом `-Dsonar.coverage.exclusions=fail.py`
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215357406-0c191807-2952-4823-af35-3ecc346b171e.png">

9. Смотрим результат в интерфейсе
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215357500-53afc7f9-5413-4bfa-9000-457d7baece06.png">

10. Исправляем ошибки, которые он выявил(включая warnings)
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215357753-f2320b00-6e03-4e4b-87d7-228a71123d01.png">

11. Запускаем анализатор повторно - проверяем, что QG пройдены успешно
12. Делаем скриншот успешного прохождения анализа, прикладываем к решению ДЗ
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215357766-94914929-0d49-475b-b437-947d6a69cb67.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215357780-be7ec830-54bf-4e15-b5c8-0d0f62aaa438.png">


## Знакомство с Nexus

### Основная часть

1. В репозиторий `maven-public` загружаем артефакт с GAV параметрами:
   1. groupId: netology
   2. artifactId: java
   3. version: 8_282
   4. classifier: distrib
   5. type: tar.gz
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215358638-2976dccd-b4ab-4a28-a98f-c74615a99cce.png">

2. В него же загружаем такой же артефакт, но с version: 8_102
3. Проверяем, что все файлы загрузились успешно
4. В ответе присылаем файл `maven-metadata.xml` для этого артефекта
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215358692-20d331f2-8556-438a-917d-34e6ebbb88f9.png">

```xml
<metadata modelVersion="1.1.0">
<groupId>netology</groupId>
<artifactId>java</artifactId>
<versioning>
<latest>8_282</latest>
<release>8_282</release>
<versions>
<version>8_102</version>
<version>8_282</version>
</versions>
<lastUpdated>20230129221623</lastUpdated>
</versioning>
</metadata>
```

### Знакомство с Maven

### Подготовка к выполнению

1. Скачиваем дистрибутив с [maven](https://maven.apache.org/download.cgi)
2. Разархивируем, делаем так, чтобы binary был доступен через вызов в shell (или меняем переменную PATH или любой другой удобный вам способ)
3. Удаляем из `apache-maven-<version>/conf/settings.xml` упоминание о правиле, отвергающем http соединение( раздел mirrors->id: my-repository-http-unblocker)
4. Проверяем `mvn --version`
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215359790-9938b8ad-efe1-4528-b8a4-4d398ed597cb.png">

6. Забираем директорию [mvn](./mvn) с pom

### Основная часть

1. Меняем в `pom.xml` блок с зависимостями под наш артефакт из первого пункта задания для Nexus (java с версией 8_282)
2. Запускаем команду `mvn package` в директории с `pom.xml`, ожидаем успешного окончания
3. Проверяем директорию `~/.m2/repository/`, находим наш артефакт
4. В ответе присылаем исправленный файл `pom.xml`
[pom.xml](https://github.com/t0hab/devops-19/blob/main/MNT-19/09-ci-03-cicd/mvn/pom.xml)
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/103331839/215362246-83452be4-8e97-4ed4-9550-a7dfd9f4a352.png">


---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
