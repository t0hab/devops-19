# Домашнее задание к занятию "11.Teamcity"

## Подготовка к выполнению

В Ya.Cloud создайте новый инстанс (4CPU4RAM) на основе образа `jetbrains/teamcity-server`
Дождитесь запуска teamcity, выполните первоначальную настройку
Создайте ещё один инстанс(2CPU4RAM) на основе образа `jetbrains/teamcity-agent`. Пропишите к нему переменную окружения `SERVER_URL: "http://158.160.29.79:8111"`

<img width="1264" alt="image" src="https://user-images.githubusercontent.com/103331839/219116697-7b29bfd0-c0f1-43e5-9607-3ada57bb3791.png">


Авторизуйте агент

<img width="1255" alt="image" src="https://user-images.githubusercontent.com/103331839/219116920-a502fd86-cd59-4473-a8ad-efc568ad029c.png">


Сделайте fork [репозитория](https://github.com/aragastmatb/example-teamcity)

<img width="1356" alt="image" src="https://user-images.githubusercontent.com/103331839/219117504-a49c6ad4-fb6b-4009-bc76-9146d8a80fc7.png">


Создать VM (2CPU4RAM) и запустить [playbook](./infrastructure)

<img width="1269" alt="image" src="https://user-images.githubusercontent.com/103331839/219118331-3c520d91-1b01-41d8-8d52-c64509670dec.png">
<img width="1231" alt="image" src="https://user-images.githubusercontent.com/103331839/219120374-6b470ade-bdb3-4dd1-b543-65148f680aef.png">



## Основная часть

Создайте новый проект в teamcity на основе fork. Сделайте autodetect конфигурации. Сохраните необходимые шаги, запустите первую сборку master'a.

<img width="1098" alt="image" src="https://user-images.githubusercontent.com/103331839/219120992-92a9fa89-42d7-4849-a275-51c74bed09af.png">
<img width="878" alt="image" src="https://user-images.githubusercontent.com/103331839/219121472-49c2f468-21db-4753-b5bb-7b592a8a757f.png">
<img width="1401" alt="image" src="https://user-images.githubusercontent.com/103331839/219121606-bfc53167-2561-4399-bd44-3c74559869a8.png">
<img width="1297" alt="image" src="https://user-images.githubusercontent.com/103331839/219121703-8fd9cff5-2504-4aa3-9f29-d9bf102bbdc5.png">
<img width="1104" alt="image" src="https://user-images.githubusercontent.com/103331839/219124068-5cb3c256-dff5-4ee5-85a4-b2b2a4f8068c.png">
<img width="1098" alt="image" src="https://user-images.githubusercontent.com/103331839/219124264-9e56adb9-fbac-4cfe-b12e-98ac58521b0c.png">


Поменяйте условия сборки: если сборка по ветке `master`, то должен происходит `mvn clean deploy`, иначе `mvn clean test`

<img width="1404" alt="image" src="https://user-images.githubusercontent.com/103331839/219126474-9b3e0746-35cc-4546-ae58-ba61f89613d4.png">


Для deploy будет необходимо загрузить [settings.xml](./teamcity/settings.xml) в набор конфигураций maven у teamcity, предварительно записав туда креды для подключения к nexus

<img width="716" alt="image" src="https://user-images.githubusercontent.com/103331839/219127951-46163f5b-7d4b-4d65-a791-24160fb4f886.png">


В pom.xml необходимо поменять ссылки на репозиторий и nexus. Запустите сборку по master, убедитесь что всё прошло успешно, артефакт появился в nexus

<img width="1075" alt="image" src="https://user-images.githubusercontent.com/103331839/219129136-07ab28c5-7892-42a3-9d6e-dcad080bcf89.png">
<img width="1184" alt="image" src="https://user-images.githubusercontent.com/103331839/219129079-ab9a6230-7bc8-4f7c-9dae-f299908084aa.png">

Мигрируйте `build configuration` в репозиторий

<img width="957" alt="image" src="https://user-images.githubusercontent.com/103331839/219130769-19f366a7-9d39-4304-9219-e36c95218915.png">


Создайте отдельную ветку `feature/add_reply` в репозитории

<img width="967" alt="image" src="https://user-images.githubusercontent.com/103331839/219132236-25ebe83a-33c0-44d5-9411-5105549b9926.png">


Напишите новый метод для класса Welcomer: метод должен возвращать произвольную реплику, содержащую слово `hunter`

[hunter](https://github.com/t0hab/example-teamcity/blob/add_reply/src/main/java/plaindoll/Welcomer.java)

Дополните тест для нового метода на поиск слова `hunter` в новой реплике

[hunter](https://github.com/t0hab/example-teamcity/blob/add_reply/src/test/java/plaindoll/WelcomerTest.java)

Сделайте push всех изменений в новую ветку в репозиторий

Сделал

Убедитесь что сборка самостоятельно запустилась, тесты прошли успешно

<img width="1084" alt="image" src="https://user-images.githubusercontent.com/103331839/219134321-136e379f-f099-4bee-a506-852b6d89fed9.png">

Внесите изменения из произвольной ветки `feature/add_reply` в `master` через `Merge`

<img width="935" alt="image" src="https://user-images.githubusercontent.com/103331839/219135710-7f529932-d72f-4747-ac1e-eea0b9aafbfd.png">

Убедитесь, что нет собранного артефакта в сборке по ветке `master`

<img width="1076" alt="image" src="https://user-images.githubusercontent.com/103331839/219136944-8c585754-5dc8-4a63-b8f5-b4069f2093b7.png">

Настройте конфигурацию так, чтобы она собирала `.jar` в артефакты сборки

<img width="914" alt="image" src="https://user-images.githubusercontent.com/103331839/219137370-2812be9f-ad7a-441f-9df5-368f354d77bd.png">

Проведите повторную сборку мастера, убедитесь, что сбора прошла успешно и артефакты собраны
Проверьте, что конфигурация в репозитории содержит все настройки конфигурации из teamcity

<img width="1090" alt="image" src="https://user-images.githubusercontent.com/103331839/219137958-c454a36d-bf4f-4084-bb4a-f128cb2dacaf.png">


[В ответ предоставьте ссылку на репозиторий](https://github.com/t0hab/example-teamcity)
